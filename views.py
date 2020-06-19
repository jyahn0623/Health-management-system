from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def welcome_msg(request):
    return HttpResponse('migrate테스팅')

def add_diet(request):
    #계속 추가 예정...
