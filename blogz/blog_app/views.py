from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Blog

# Create your views here.

def test_function(request):
    return HttpResponse("<h1>Hello World<h1>")

def home_view(request):
    blogs = Blog.objects.all()
    data = {
        'blogdata': blogs
    }
    return render(request, 'home.html', context=data)

def add_blog(request):
    return render(request, 'add_blog.html', context={})

def save_blog(request):
    title = request.POST['title']
    author = request.POST['author']
    date = request.POST['date']
    content = request.POST['content']

    print("Title : ", title)
    print("Author : ", author)
    print("Date : ", date)
    print("Content : ", content)

    blog = Blog(title=title, author=author, date=date, content=content)
    blog.save()
    return redirect('home')
    
def delete_blog(request, blog_id):
    blog = Blog.objects.filter(pk = blog_id)
    blog.delete()
    return redirect('home')

def get_blog_info(request, blog_id):
    blogs = Blog.objects.get(pk = blog_id)
    data = {
        'blog': blogs
    }
    
    return render(request, 'get_blog_info.html', context=data)
    
    
def update_blog(request, blog_id):
    blog = Blog.objects.get(pk = blog_id)
    blog.title = request.POST['title']
    blog.author = request.POST['author']
    blog.date = request.POST['date']
    blog.content = request.POST['content']

    blog.save()
    return redirect('home')