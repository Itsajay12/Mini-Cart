from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=="POST":
        uname=request.POST['uname']
        passw=request.POST['password']
        cpassw=request.POST['cpassword']
        email=request.POST['email']
        if passw==cpassw:
            if User.objects.filter(username=uname).exists()or User.objects.filter(email=email).exists():
                messages.error(request,'Username/Email Already Exists')
            else:
                query=User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],username=uname,email=email,password=passw)
                query.set_password(passw)
                query.save()
                return redirect(login)
        else:
            messages.info(request,'Password Dont MAtch')
            return redirect(register)


    return render(request,'register.html')
def login(request):
    return render(request,'login.html')