from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required


# from requests import request

# import accounts

# Create your views here.
def index(request):
    # print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request,'accounts/index.html')

def login1(request):
    if request.user.is_anonymous:
        return render(request,'accounts/login.html')
    else:
        return redirect('/')

def loginuser(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username,password)

            user = authenticate(username=username, password=password)
            print(request.user)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect("/")
            else:
                # No backend authenticated the credentials
                return render(request,'accounts/login.html')

        return render(request,'login.html')
    else:
        return redirect('/')


@login_required
def logoutuser(request):
    logout(request)
    return redirect('/login')