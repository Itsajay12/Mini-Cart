from django.shortcuts import render,redirect
from .models import *
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
                return redirect(delivery_details)
        else:
            messages.warning(request,"Null Values are not allowed")
    return render(request,'login.html')
@login_required(login_url="/login")
def delivery_details(request):
    try:
        existing_delivery_address = DeliveryAddress.objects.get(username=request.user)
        
        if existing_delivery_address:
            return render(request, 'index.html')
        else:
            if request.method == "POST":
                mob = request.POST['mob']
                alt_mob = request.POST['altermob']
                pincode = request.POST['pincode']
                address = request.POST.get('address')
                state = request.POST.get('state')
                country = request.POST.get('country')
                deliverytype = request.POST.get('dt')

                if mob and alt_mob and pincode and address and state and country and deliverytype:
                    query = DeliveryAddress.objects.create(
                        username=request.user,
                        mobile=mob,
                        altmob=alt_mob,
                        pincode=pincode,
                        address=address,
                        dtype=deliverytype,
                        state=state,
                        country=country
                    )
                    query.save()
                    messages.success(request, "Delivery address added successfully.")
                    return render(request, 'index.html')
                else:
                    messages.info(request, "No fields can have null values.")
            return render(request, 'order.html')
    except DeliveryAddress.DoesNotExist:
        if request.method == "POST":
            mob = request.POST['mob']
            alt_mob = request.POST['altermob']
            pincode = request.POST['pincode']
            address = request.POST.get('address')
            state = request.POST.get('state')
            country = request.POST.get('country')
            deliverytype = request.POST.get('dt')

            if mob and alt_mob and pincode and address and state and country and deliverytype:
                query = DeliveryAddress.objects.create(
                    username=request.user,
                    mobile=mob,
                    altmob=alt_mob,
                    pincode=pincode,
                    address=address,
                    dtype=deliverytype,
                    state=state,
                    country=country
                )
                messages.success(request, "Delivery address added successfully.")
                return render(request, 'index.html')
            else:
                messages.info(request, "No fields can have null values.")
        return render(request, 'order.html')
    except Exception as e:
        messages.warning(request, f"Error occurred: {e}")
        return render(request, 'order.html') 
def logout_user(request):
    if request.method=="POST":
        
        logout(request)
    return redirect('login')

def product_page(request,category):
    query=Products.objects.filter(category=category)
    

    return render(request,'product_page.html',{"query":query})
@login_required(login_url='/login')
def add_cart(request,item):
    query=Products.objects.filter(pro_name=item)
    if query:
        print("called",query.pro_name)
        query2=Cart.objects.create(username=request.user,item_name=query.pro_name,item_price=query.pro_price)