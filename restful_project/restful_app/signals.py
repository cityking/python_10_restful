#coding: utf-8
from django.dispatch import Signal, receiver
from django.db.models.signals import pre_save, post_save
from .models import Poem

#定义信号
signalCity = Signal(providing_args = ['city'])

#定义接收器receiver的回调函数
@receiver(signalCity)
def signal_callback(sender, **kwargs):
	print(sender,kwargs)
	print('signal_callback called')

@receiver(signalCity)
def signal_callback1(sender, **kwargs):
	print(sender,kwargs)
	print('signal_callback called1')

#注册信号
#signalCity.connect(signal_callback)
#signalCity.connect(signal_callback1)

@receiver(pre_save, sender=Poem)
def pre_save_call_back(sender, **kwargs):
	print('pre_save_call_back', sender)

@receiver(post_save)
def post_save_call_back(sender, **kwargs):
	print('post_save_call_back')
