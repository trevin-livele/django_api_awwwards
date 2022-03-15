from django.shortcuts import redirect, render,get_object_or_404
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate


# Create your views here.

def register(request):
    return render(request, 'accounts/register.html')


def login_user(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('login')
