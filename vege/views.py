from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your views here.
@login_required(login_url="/login/")
def receipe(request):
    if request.method=="POST":
        data=request.POST
        receipe_image=request.FILES.get("receipe_image")
        receipe_name=data.get("receipe_name")
        receipe_description=data.get("receipe_description")
        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description
        )
        return redirect("/receipe")
    queryset=Receipe.objects.all()
    if request.GET.get("Search"):
        queryset=queryset.filter(receipe_name__icontains=request.GET.get("Search"))
    context={"receipe":queryset}

    return render(request,"receipe.html",context)

@login_required(login_url="/login/")
def delete_receipe(request,id):
    Queryset=Receipe.objects.get(id=id)
    Queryset.delete()
    return redirect("/receipe/")

@login_required(login_url="/login/")
def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        receipe_image=request.FILES.get("receipe_image")
        receipe_name=data.get("receipe_name")
        receipe_description=data.get("receipe_description")
        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description

        if receipe_image:
            queryset.receipe_image=receipe_image
        queryset.save()
        return redirect('/receipe/'
        )
    context={'receipe':queryset}
    return render(request,"update_receipe.html",context)


def register(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=User.objects.filter(username=username)
        if (user.exists()):
            messages.info(request,"Username Already Taken")
            return redirect("/register/")

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.info(request,"Account Created Successfully")
        return redirect("/register/")
    return render(request,"register.html")

def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/')
        else:
            auth_login(request,user)
            return redirect('/receipe/')
    return render(request,'login.html')

def logout(request):
    return redirect("/login/")