#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import PoemSerializer
from .models import Poem
from rest_framework.decorators import api_view
from .signals import signalCity,signal_callback

# Create your views here.
def home(request):
	#触发信号
	signalCity.send(sender=None, city="hello")	
	return HttpResponse("hello world")

def disconnect(request):
	#注销信号
	signalCity.disconnect(signal_callback)
	return HttpResponse("hello world")

class PoemListView(APIView):
	def get(self, request, format=None):
		poems = Poem.objects.all()
		serializer = PoemSerializer(poems, many=True)
		return Response(serializer.data)
	def post(self, request, format=None):
		serializer = PoemSerializer(data=request.data, many=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','PUT','DELETE'])
def poem_detail(request, pk):
	try:
		poem = Poem.objects.get(pk=pk)
	except Poem.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = PoemSerializer(poem)
		return Response(serializer.data)
	if request.method == 'PUT':
		serializer = PoemSerializer(poem, request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
	if request.method == 'DELETE':
		poem.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
