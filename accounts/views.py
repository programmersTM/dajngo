from django.shortcuts import render, redirect
from django.contrib import auth

# from .forms import CustomChange, CustomCreate
from .models import CustomUser

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
    
    return render(request, 'register/dashboard.html')