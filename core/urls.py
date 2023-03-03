"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token
from django_dyn_dt.datatb import DataTB, export

urlpatterns = [
    path('', include('home.urls')),
    path("admin/", admin.site.urls),

    path("api/",   include("api.urls")),        # <-- NEW (Used by API GEN)
    path('login/jwt/', view=obtain_auth_token), # <-- NEW (Used by API GEN)
    
    path('datatb/<str:model_name>/<int:pk>/', csrf_exempt(DataTB.as_view())),    # <-- NEW: (Used by Dynamic DataTables)
    path('datatb/<str:model_name>/', csrf_exempt(DataTB.as_view())),    # <-- NEW: (Used by Dynamic DataTables)
    path('datatb/<str:model_name>/export/', csrf_exempt(export)),    # <-- NEW: (Used by Dynamic DataTables)

    path("", include('admin_adminlte.urls')),
]
