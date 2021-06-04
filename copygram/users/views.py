from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from users.models import Profile

def logginView(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('feed')
        else:
            return render(request,'users/login.html',{'error':'invalid username or password'})
    return render(request, 'users/login.html' )


@login_required
def logoutView(request):
    logout(request)
    return redirect('login')

def signupView(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST.get('paswrd',True)
        cpassword=request.POST.get('paswrdc',True)
        email=request.POST['email']
        if cpassword!=password:
            return render(request,'users/signup.html',{'error':'Password confirmation do not match'})
        try:
            user=User.objects.create_user(username=username,email=email,password=password)
        except IntegrityError:
            return render(request,'users/signup.html',{'error':'Username already in use'})
        user.first_name= request.POST['fname']
        user.last_name=request.POST['lname']
        user.save()
        profile = Profile(user=user)
        profile.save()
        return redirect('login')
    return render(request,'users/signup.html')

    