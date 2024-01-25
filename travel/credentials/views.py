from urllib import request

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password= request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info("NO such user")
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        name=request.POST['username']
        first= request.POST['firstname']
        last = request.POST['lastname']
        email= request.POST['email']
        password = request.POST['password']
        cpassword= request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=name).exists():
                messages.info(request,"username alredy exists")
                return redirect(register)
            elif User.objects.filter(first_name=first).exists():
                messages.info(request,"first name alredy exists")
                return redirect(register)
            elif User.objects.filter(last_name=last).exists():
                messages.info(request,"last name alredy exists")
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email alredy exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=name,first_name=first,last_name=last,email=email,password=password)
                user.save();
                return redirect('login')
                print('User created')
        else:
            messages.info(request,'password Not natched')
            return redirect('register')

        return redirect('/')

    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')