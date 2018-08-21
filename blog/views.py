from django.shortcuts import render, get_object_or_404
from . models import Blog_Post
def all_posts(request):
    blogs = Blog_Post.objects
    return render(request, 'blog/home.html', {'blogs':blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog_Post, pk=blog_id) # uses primary key to search database. We get blog_id got from urls.py
    return render(request,'blog/detail.html', {'blog':detailblog})	