from django.shortcuts import render
from django_dyn_dt.datatb import DataTB
from django.http import HttpResponse

# Create your views here.

ddt = DataTB(model_class_path="home.models.Product")


def index(request):
    # Page from the theme
    return render(request, 'pages/index.html')


def test_datatb(request, **kwargs):
    return render(request, 'test-datatb.html', context={
        'data_table1': ddt.render(),
    })

def api_generator(request):
    return render(request, 'pages/api-generator.html')

def dyn_datatb(request):
    return render(request, 'pages/dyn-datatb.html')
