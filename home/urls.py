from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test-datatb/', views.test_datatb)
]
