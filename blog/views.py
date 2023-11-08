from django.shortcuts import render


from blog.models import Blog

def index(request):

    blogs = Blog.objects.filter(published = 'pub').order_by('-date_created')

    context = {
        'blogs': blogs
    }

    return render(request, 'pages/home.html', context)

def new_blog(request):
    
    return render(request, 'blog/new_blog.html')