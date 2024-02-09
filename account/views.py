from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid USer & Pass')
            return redirect('signin')
    return render(request,'account/signin.html')


def signup(request):
    if request.method == 'POST':  # Fix the typo here
        nm = request.POST.get('name')
        un = request.POST.get('username')
        pw = request.POST.get('password')

        if User.objects.filter(username=un).exists():  # Fix the typo here
            messages.error(request, 'Username already exists')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=un, password=pw)
            user.save()
            messages.success(request, 'Account created successfully. Please sign in.')
            return redirect('signin')

    return render(request, 'account/signup.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
