"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from . import views
from ecommerce.views import Maintenance, maintenance, NotFound, Homepage, UserCreationView

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('Maintenance', Maintenance.as_view(), name = 'Maintenance'),
    path('maintenance/<int:cheneso>',maintenance,name='maintenance'),
    path('404-not-found', NotFound.as_view(), name='404-not-found'),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('register/', UserCreationView.as_view(), name='user-create')
]
