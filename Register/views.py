from django.shortcuts import render,redirect
from .form import *
from .models import *
# Create your views here.


def Staff_Register(request):
    form=StaffRegister()
    if request.method == "POST":
        form=StaffRegister(request.POST)
        if form.is_valid():
            staff=form.save(commit=False)
            staff.set_password(form.cleaned_data['password'])
            staff.save()
            all_staff_list=All_Staff_List(username = staff.username,
                                          email = staff.email,
                                          join_date = staff.date_joined,
                                          staff_reference_id= staff.id )
            all_staff_list.save()
            return redirect('staff_login') 
    return render(request,'staff_register_form.html',{'form':form})



def Institute_Register(request):
    form=InstituteRegister()
    if request.method == "POST":
        form=InstituteRegister(request.POST)
        if form.is_valid():
            institute=form.save(commit=False)
            institute.set_password(form.cleaned_data['password'])
            institute.save()
            all_institute_list=All_Institute_List(username = institute.username,
                                                  email = institute.email,
                                                  join_date = institute.date_joined,
                                                  institute_reference_id= institute.id )
            all_institute_list.save()            
            return redirect('institute_login')    
    return render(request,'institute_register_form.html',{'form':form})