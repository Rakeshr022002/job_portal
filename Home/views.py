from django.shortcuts import render,redirect
from .models import *
import os
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='staff_login')
def Home(request):
    context ={'all_post' : Staff_data.objects.filter(staff_reference_id = request.user),
              'institute':Institute_data.objects.filter(institute_reference_id = request.user),
              'all_staff_details':Staff_data.objects.all(),
              'all_institute_list':Institute_data.objects.all()}
    
    if request.method == 'POST':
        education = request.POST.get('education')
        role = request.POST.get('jobrole')
        Qulification=request.POST.get('qulification')
        Role=request.POST.get('role')

        
        if education :
          context={'all_staff_details':Staff_data.objects.filter(Education = education)}
          
        elif Qulification:
            context={'all_institute_list':Institute_data.objects.filter(qulification = Qulification)}   
          
        if role :
          context={'all_staff_details':Staff_data.objects.filter(search_role = role)}
        
        elif Role:  
            context={'all_institute_list':Institute_data.objects.filter(job_role = Role)}  
  

    return render(request,'home.html',context)


@login_required(login_url='staff_login')
def staff_info(request):
    if request.method == "POST":
        staff_data = Staff_data(name=request.POST.get('name'),
                                email=request.POST.get('email'),
                                mobile_no=request.POST.get('mobileno'),
                                date_of_birth=request.POST.get('dateofbirth'),
                                gender=request.POST.get('gender'),
                                Education=request.POST.get('education'),
                                country=request.POST.get('country'),
                                state=request.POST.get('state'),
                                search_role=request.POST.get('jobrole'),
                                experience=request.POST.get('experience'),
                                remote=request.POST.get('remote'))
        if len(request.FILES) !=0:
            staff_data.Staff_img=request.FILES['staff-img']
            
        staff_data.staff_reference = request.user   
        staff_data.save()
        return redirect('staff_view') 
            
    return render(request,'staff_info_form.html')

@login_required(login_url='staff_login')
def staff_info_view(request):
    context ={'all_post' : Staff_data.objects.filter(staff_reference_id = request.user)}
    return render(request,'staff_info_view_form.html',context)


@login_required(login_url='staff_login')
def staff_update(request,id):
    update_staff=Staff_data.objects.get(id = id)
    if request.method == 'POST':
        
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobileno')
        dob=request.POST.get('dateofbirth')
        gender=request.POST.get('gender')
        education=request.POST.get('education')
        country=request.POST.get('country')
        state=request.POST.get('state')
        role=request.POST.get('jobrole')
        experience=request.POST.get('experience')
        remote=request.POST.get('remote')
        
        update_staff.name=name
        update_staff.email=email
        update_staff.mobile_no=mobile
        update_staff.date_of_birth=dob
        update_staff.gender=gender
        update_staff.Education=education
        update_staff.country=country
        update_staff.state=state
        update_staff.search_role=role
        update_staff.experience=experience
        update_staff.remote=remote
        
        if len(request.FILES)!=0:
            if len(update_staff.Staff_img)>0:
                os.remove(update_staff.Staff_img.path)
            update_staff.Staff_img = request.FILES['staff-img']
        
        update_staff.save() 
        print(update_staff)
        
        return redirect('staff_view')   
                

    return render(request,'staff_info_form.html',{'data': update_staff})
    

@login_required(login_url='staff_login')
def staff_delete(request,id):
    
    delete_staff=Staff_data.objects.get(id = id)
    
    if len(delete_staff.Staff_img)>0:
        os.remove(delete_staff.Staff_img.path)
        
    delete_staff.delete()
    
    return redirect('staff_view')
    
@login_required(login_url='institute_login')   
def post_job(request):
    if request.method == "POST":
        institute_data = Institute_data(
                        name = request.POST.get('ins-name'),
                        email = request.POST.get('ins-email'),
                        website = request.POST.get('ins-website'),
                        department = request.POST.get('ins-dept'),
                        job_role = request.POST.get('ins-job-role'),
                        job_type = request.POST.get('ins-job-type'),
                        salary = request.POST.get('ins-salary'),
                        number_of_position = request.POST.get('ins-position'),
                        qulification = request.POST.get('ins-qulification'),
                        experience = request.POST.get('ins-experience'),
                        job_description = request.POST.get('ins-description'),
                        address = request.POST.get('ins-address'),
                        last_apply_data = request.POST.get('ins-date'),
                        interview_mode = request.POST.get('ins-interview'),)
        
        if len(request.FILES) !=0:
            institute_data.institute_img=request.FILES['ins-img']
            
        institute_data.institute_reference = request.user
        
        institute_data.save()
        return redirect('/home')      
                
    return render(request,'institute_post_job.html')   
    
@login_required(login_url='institute_login')  
def job_list(request):
    context={'all_job':Institute_data.objects.filter(institute_reference_id = request.user)}

    if request.method == "POST":
        dept_name=request.POST.get('deptname')
        job_role=request.POST.get('jobrole')
        
        if dept_name:
            context={'all_job':Institute_data.objects.filter(department = dept_name)}
        if job_role :
            context={'all_job':Institute_data.objects.filter(job_role = job_role)}
                             
    return render(request,'institute_job_list.html',context)    
  

@login_required(login_url='institute_login')  
def job_delete(request,id):
    
    delete_job = Institute_data.objects.get(id = id)
    if len(delete_job.institute_img)>0:
        os.remove(delete_job.institute_img.path)
        
    delete_job.delete()
    
    return redirect('job_list')


@login_required(login_url='institute_login')  
def job_update(request,id):
    
    update_job = Institute_data.objects.get(id = id)
    
    if request.method == "POST":
        name = request.POST.get('ins-name'),
        email = request.POST.get('ins-email'),
        website = request.POST.get('ins-website'),
        department = request.POST.get('ins-dept'),
        job_role = request.POST.get('ins-job-role'),
        job_type = request.POST.get('ins-job-type'),
        salary = request.POST.get('ins-salary'),
        number_of_position = request.POST.get('ins-position'),
        qulification = request.POST.get('ins-qulification'),
        experience = request.POST.get('ins-experience'),
        job_description = request.POST.get('ins-description'),
        address = request.POST.get('ins-address'),
        last_apply_data = request.POST.get('ins-date'),
        interview_mode = request.POST.get('ins-interview')
        
        
        update_job.name=name
        update_job.email=email
        update_job.website=website
        update_job.department=department
        update_job.job_role=job_role
        update_job.job_type=job_type
        update_job.salary=salary
        update_job.number_of_position=number_of_position
        update_job.qulification=qulification
        update_job.experience=experience
        update_job.job_description=job_description
        update_job.address=address
        update_job.last_apply_data=last_apply_data
        update_job.interview_mode=interview_mode
        
        if len(request.FILES)!=0:
            if len(update_job.institute_img)>0:
                os.remove(update_job.institute_img.path)
            update_job.institute_img = request.FILES['ins-img']
            
        update_job.save()
        
        return redirect('job_list')   
        
        
    return render(request,'institute_post_job.html',{'data':update_job})        