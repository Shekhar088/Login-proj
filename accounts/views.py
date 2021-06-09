from django.http.request import RAISE_ERROR
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password ==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is taken")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email is taken")
                else:
                    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
                    user.save()
                    messages.success(request,"You can now log in.")
                    return redirect('login')
        else:
            messages.error(request,"Password donot match")
    return render(request, "accounts/register.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user  = auth.authenticate(username= username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"You are now logged in.")
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('login')
    return render(request, "accounts/login.html",)

def logout(request):
    if request.method =="POST":
        auth.logout(request)
        print("logged out")
        return redirect("/")

def dashboard(request):

    return render(request, "accounts/dashboard.html",)