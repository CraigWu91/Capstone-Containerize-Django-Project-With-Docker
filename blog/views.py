from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required
# Create your views here.
def header(request):
    '''
    Renders blog post html template with list of all blog posts

    param: request: http request

    return: http response with blog html content
    '''
    object_list = Post.objects.all()
    return render(request, "blog/blog.html", {"blog": object_list})

