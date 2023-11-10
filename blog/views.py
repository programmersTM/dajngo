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
        if (title != "") and (text != ""):
            blog = Blog.objects.create(author = author, title=title, text=text)
            blog.save()
            return redirect('index', )
    return render(request, 'blog/new_blog.html')


def detail_blog(request, title):
    blog = get_object_or_404(Blog, title = title)
    user = auth.get_user(request)
    if request.method == 'POST':
        author = user.username
        author = CustomUser.objects.get(username = author)
        email = user.email
        text = request.POST['text']
        if user != "" and email !="" and text != "":
            new_comment = Comment.objects.create(author_comment= author, post=blog, email=email, comment_text=text)
            new_comment.save()

    comments = Comment.objects.filter(post= blog).order_by('-date_created')
    context = {
        'blog': blog,
        'comments': comments
    }

    return render(request, 'blog/detail.html', context)
