from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')

def api_generator(request):
    return render(request, 'pages/api-generator.html')

def dyn_datatb(request):
    return render(request, 'pages/dyn-datatb.html')
