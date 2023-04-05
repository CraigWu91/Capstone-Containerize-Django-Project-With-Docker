from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def index(request):
    return render(request, "craigcv.html")

def index(request):
    return render(request, "craigcvnocss.html")
