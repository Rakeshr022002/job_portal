from django.shortcuts import render,redirect
from .form import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def stafflogin(request):
    form = StaffLogin()
    if request.method == 'POST':
        form = StaffLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user  = authenticate(username = username,password = password)
            # print(user.is_staff)
            if user is not None:
                if user.is_staff==True:
                  login(request,user)
                  return redirect('/home')
    return render(request,'staff_login.html',{'form':form})



def institutelogin(request):
    form = InstituteLogin()
    if request.method == 'POST':
        form = InstituteLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user  = authenticate(username = username,password = password)
            if user is not None:
                if user.is_staff==False:
                  login(request,user)
                  return redirect('/home')    
    return render(request,'institute_login.html',{'form':form})





def logoutuser(request):
    
    logout(request)
    
    return redirect('intro_page')
    
