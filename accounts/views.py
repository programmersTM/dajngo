from django.shortcuts import render, redirect
from django.contrib import auth

# from .forms import CustomChange, CustomCreate
from .models import CustomUser
from blog.models import Blog, Comment

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if CustomUser.objects.filter(username=username).exists():
                return redirect('signup')
            else:
                user = CustomUser.objects.create_user(username=username, email=email, password=password)
                user.save() 
                return redirect('login')
        else:
            return redirect('signup')

    return render(request, 'register/signup.html')
    
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if CustomUser.objects.filter(username=username).exists():
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('index')
        else:
            return redirect('login')
    return render(request, 'register/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    user = auth.get_user(request)
    blogs = Blog.objects.filter(author = user).order_by('-date_created')
    comments = Comment.objects.filter(author_comment = user).order_by('-date_created')

    # count object and set number near
    def make_num_obj(list_object):
        obj_list = []
        i = 1
        for val in list_object:
            obj_list.append((i, val))
            i += 1
        return obj_list
        
    blogs_new = make_num_obj(blogs)
    commentlist_new = make_num_obj(comments)

    context = {
        'blogs': blogs_new,
        'comments': commentlist_new,
        # 'number_blogs': blog_count,
        # 'number_comments': comment_count,
    }



    return render(request, 'register/dashboard.html', context)

