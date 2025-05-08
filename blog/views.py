from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.order_by('date')[:4]
    context ={
        'data' : blogs
    }
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def blog(request):
    blogs = Blog.objects.all()
    context ={
        'data' : blogs
    }
    return render(request,'blog.html', context)
def blogcontent(request, pk):
    content = Blog.objects.get(pk=pk)
    context ={
        'data': content
    }
    return render(request, 'blogcontent.html', context)