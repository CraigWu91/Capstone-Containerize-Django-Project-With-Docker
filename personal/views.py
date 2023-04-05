from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
def index(request):
    '''
    Renders index html template that is the shopping page

    param: request: http request

    return: http response with index html content
    '''
    return render(request, "index.html")

def index(request):
    '''
    Renders craigcv html template that is also the homepage

    param: request: http request

    return: http response with craigcv html content
    '''
    return render(request, "craigcv.html")

def index(request):
    '''
    Renders craigcvnocss html template

    param: request: http request

    return: http response with craigcvnocss html content
    '''
    return render(request, "craigcvnocss.html")
