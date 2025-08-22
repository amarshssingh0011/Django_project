from django.shortcuts import render
from .models import post
from django.http import HttpResponse

# Create your views here.

def blog_index(request):
    return render(request = request, template_name = 'blog_index.html')

def get_posts(request):
    all_posts = post.objects.all()
    return render(request = request, template_name = 'posts.html', context = {'posts': all_posts})
def create_post(request):
    return render(request, 'blog/create_post.html'),