from django.shortcuts import render, redirect
from .models import Product_model
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def homepage(request):
    context={'product': Product_model.objects.all()}
    return render(request, 'shop/home.html', context=context)


def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('با موفقیت وارد شدید.'))
            return redirect('shop:home')
        else:
            messages.success(request, ('ورود شما با مشکلی رو به رو شده است.'))
            return redirect('shop:login')
    else:
        return render(request, 'shop/signin.html')

def logout_user(request):
    logout(request)
    messages.success(request, ('با موفقیت خارج شدید.'))
    return redirect('shop:home')
    #context={}
    #return render(request, 'shop/signout',)
