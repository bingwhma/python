# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	return HttpResponse("Hello world")
	
def hello2(request):
    context          = {}
    context['hello'] = 'Hello World! into template '
    return render(request, 'hello2.html', context)