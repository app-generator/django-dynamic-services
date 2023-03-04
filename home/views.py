from django.shortcuts import render
from django_dyn_dt.datatb import DataTB
from django.http import HttpResponse

# Create your views here.

def index(request):
    # Page from the theme
    return render(request, 'pages/index.html')

def api_generator(request):
    return render(request, 'pages/api-generator.html')

def dyn_datatb(request):

    context = {} 
        
    ddt = DataTB(model_class_path="home.models.Product")
    context['data_table1'] = ddt.render()

    return render(request, 'pages/dyn-datatb.html', context=context)
