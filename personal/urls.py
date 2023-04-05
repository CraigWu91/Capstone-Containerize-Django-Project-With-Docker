from django.urls import path, include
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('accounts/', include('django.contrib.auth.urls')),
]