from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup (request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password_confirm']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'acounts/signup.html',{'error':'user alredy'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'acounts/signup.html',{'error':'password must be match'})

    else:
        return render(request,'acounts/signup.html')

def login (request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'] , password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'acounts/login.html',{'error':'username or password is incorrect'})
    else:
        return render(request,'acounts/login.html')

def logout (request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

    else:
        return render(request,'acounts/signup.html')
