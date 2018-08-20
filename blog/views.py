from django.shortcuts import render
from . models import Blog_Post
def all_posts(request):
    blogs = Blog_Post.objects
    return render(request, 'blog/home.html', {'blogs':blogs})

# Create your views here.
