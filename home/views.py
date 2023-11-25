from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
# Create your views here.
@login_required(login_url="/login")
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
                messages.success(request,"Succesfully Registered")
                return redirect(login_user)
        else:
            messages.info(request,'Password Dont MAtch')
            return redirect(register)


    return render(request,'register.html')
def login_user(request):
    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['password']
        if username !="" and password!="":
            query=authenticate(request,username=username,password=password)
            if query is None:
                messages.error(request,"Invalid Credentials")
            else:
                login(request,query)
                return redirect(index)
        else:
            messages.warning(request,"Null Values are not allowed")
    return render(request,'login.html')
def delivery_details(request):
    if request.method=="POST":
        mob=request.POST['mob']
        alt_mob=request.POST['altermob']
        pincode=request.POST['pincode']
        address=request.POST['address']
    return render(request,'order.html')
def logout_user(request):
    if request.method=="post":
        print("called")
        logout(request)
    return redirect(login_user)
