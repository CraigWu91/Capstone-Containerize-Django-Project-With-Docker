from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required
# Create your views here.
def header(request):
    object_list = Post.objects.all()
    return render(request, "blog/blog.html", {"blog": object_list})

