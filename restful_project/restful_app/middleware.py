try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object 
from django.http import HttpResponse


class CheckSourceMiddleware(MiddlewareMixin):
	def process_request(self, request):
		from_source = request.META['HTTP_USER_AGENT']
		print('from source:', from_source)
		if 'Android' in from_source:
			request.session['from_source'] = 'Android'
		else:
			request.session['from_source'] = 'pc'
	def process_response(self, request, response):
		return HttpResponse("CheckSourceMiddleware response")


class ForbidSomeIpMiddleware(MiddlewareMixin):
	def process_request(self, request):
		allow_ip = ['127.0.0.1',]
		ip = request.META['REMOTE_ADDR']
		print('ip', ip)
		if ip in allow_ip:
			print('ip not allowed')
			return HttpResponse('ip not allowed')
		
	def process_response(self, request, response):
		return HttpResponse("ForbidSomeIpMiddleware response")
