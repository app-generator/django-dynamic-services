import django.urls
from django.views.decorators.csrf import csrf_exempt

from api.views import *


urlpatterns = [

	django.urls.re_path("product/((?P<pk>\d+)/)?", csrf_exempt(ProductView.as_view())),
	django.urls.re_path("sales/((?P<pk>\d+)/)?", csrf_exempt(SalesView.as_view())),

]