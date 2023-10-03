from django.shortcuts import render , redirect
from .models import Feature
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    features=Feature.objects.all()
    return render(request,'index.html',{'features':features})


def counter(request):
    posts=['abstar','abhijeet',2,'sachin','manchu']
    return  render(request,'counter.html',{'posts':posts}) # we render to counter.html while taking input from index.html using words of textarea name

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            
            else:
                user=User.objects.create_user(username=username, email=email,password=password)
                user.save()
                return redirect('login')
        
        else:
            messages.info(request,'Password is not same')
            return redirect('register')
        
    else:
        return render(request, 'register.html')

    


def post(request,pk):
    return render(request, 'post.html', {'pk':pk})

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Are Invalid/wrong')

    else:
        return render(request, 'login.html')
