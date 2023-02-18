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
