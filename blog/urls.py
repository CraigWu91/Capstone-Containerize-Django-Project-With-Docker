from django.views.generic import ListView, DetailView
from django.urls import path
from .models import Post
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',
         login_required(ListView.as_view(
             queryset=
             Post.objects.all().order_by("-date")[:25],
             template_name="blog.html"
         )
         )),

    path('<int:pk>/',
         DetailView.as_view(
             model=Post,
             template_name="post.html"
         )
         ),
    path('', views.header, name='blog'),
] 