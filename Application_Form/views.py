from django.shortcuts import render,redirect
from Home.models import *
from .models import*
from django.contrib import messages
from .models import *
import os
# Create your views here.


def institute_overview(request,id):
    context={'data':Institute_data.objects.filter(id = id)}
    return render(request,'institute_overview.html',context)



def institute_application(request,id):
    context={'data':Institute_data.objects.filter(id = id)}
    if request.method =='POST':
        applied_job=staff_applied_job(
            fullname=request.POST.get('fullname'),
            email=request.POST.get('email'),
            phone_no=request.POST.get('phone'),
            gender=request.POST.get('gender'),
            dob=request.POST.get('dob'),
            address=request.POST.get('address'),
            Education=request.POST.get('education'),
            job_role=request.POST.get('job_role'),
            experience=request.POST.get('experience'),
            institute_reference=request.POST.get('ins_refernce'),)
        
        if len(request.FILES) !=0:
            applied_job.resume=request.FILES['resume']
            
        applied_job.staff_reference=request.user
        
        applied_job.save()
        messages.success(request,"Job Apply Successfully!")
        return redirect('home_page')    
    
    return render(request,'institute_application.html',context)


def applied_job(request):
    context = {'data':staff_applied_job.objects.filter(institute_reference = request.user.id)} 
    if request.method == 'POST':
        jobrole=request.POST.get('jobrole')
        if jobrole:
            context={'data':staff_applied_job.objects.filter(job_role = jobrole)}
    return render(request,'applied_job.html',context)



def applied_staff(request,id):
    context = {'data':staff_applied_job.objects.filter(id = id)} 
    return render(request, 'applied_staff_overview.html',context)


def delete_applied_staff(request,id):
    del_applied_staff= staff_applied_job.objects.get(id = id)
    
    if len(del_applied_staff.resume)>0:
        os.remove(del_applied_staff.resume.path)
        
        del_applied_staff.delete()
        
        return redirect('applied_job') 

    

    
def staff_overview(request,id):
    context={'data':Staff_data.objects.filter(id = id)}
    return render(request,'staff_overview.html',context)    


def hire_mail(request,id):
    context={'data':Staff_data.objects.filter(id = id),}
    if request.method =='POST':
        hire_staff = institute_hire_staff(
             institute_name=request.POST.get('ins-name'),
             email=request.POST.get('ins-email'),
             phoneo_no=request.POST.get('ins-phone'),
             address=request.POST.get('ins-address'),
             hire_role=request.POST.get('hire-role'),
             salary=request.POST.get('ins-salary'),
             subject=request.POST.get('ins-subject'),
             hire_staff=request.POST.get('staff_ref'))
        
        hire_staff.institute_reference = request.user
        
        hire_staff.save()
        return redirect('home_page')
    return render(request,'hire_mail.html',context)


def hired_job_view(request):
    context={'data':institute_hire_staff.objects.filter(hire_staff = request.user.id)}
    return render(request,'hired_job_view.html',context)



def hired_job_see(request,id):
    context={'data':institute_hire_staff.objects.filter(id = id)}
    return render(request,'hired_job_see.html',context)


def hired_job_delete(request,id):
    del_job=institute_hire_staff.objects.filter(id = id)
    
    del_job.delete()
    
    return redirect('hired_job_view')
    