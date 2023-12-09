from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth

from accounts.models import CustomUser
from .models import Blog, Comment

def index(request):

    blogs = Blog.objects.filter(published = 'pub').order_by('-date_created')
    context = {
        'blogs': blogs
    }

    return render(request, 'pages/home.html', context)

def new_blog(request,):
    
    author = auth.get_user(request)
    if request.method == 'POST':
        author = CustomUser.objects.get(username=author)
        title = request.POST['title']
        text = request.POST['text']
        status = request.POST['status']
        if title  and text  and status :
            blog = Blog.objects.create(author = author, title = title, text = text, published = status)
            blog.save()
            return redirect('index')
    return render(request, 'blog/new_blog.html')


def detail_blog(request, title):
    blog = get_object_or_404(Blog, title = title)
    user = auth.get_user(request)
    if request.method == 'POST':
        author = user.username
        author = CustomUser.objects.get(username = author)
        email = user.email
        text = request.POST['text']
        if user and email and text :
            new_comment = Comment.objects.create(author_comment= author, post=blog, email=email, comment_text=text)
            new_comment.save()
            return redirect('detail_blog', title)

    comments = Comment.objects.filter(post= blog).order_by('-date_created')
    context = {
        'blog': blog,
        'comments': comments
    }

    return render(request, 'blog/detail.html', context)


def edit_blog(request, pk):
    blog = Blog.objects.get(id = pk)

    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        status = request.POST['status']
        if title and text and status:
            Blog.objects.filter(id= pk).update(title=title, text=text, published= status)
            blog_new = Blog.objects.get(id = pk)
            return redirect('detail_blog', blog_new.title)
    context = {
        "blog": blog
    }

    return render(request, 'blog/new_blog.html', context)


def delete_blog(request, pk):
    blog = Blog.objects.get(id = pk)
    
    if request.method == 'POST':
        choice = request.POST['status']
        if choice == 'yes':
            blog.delete()
            return redirect('index')
        else:
            return redirect('detail_blog', blog.title)

    context = {
        'blog':blog,
    }
    return render(request, 'blog/delete.html', context)


def about_blog(request):
    return render(request, 'pages/about.html')