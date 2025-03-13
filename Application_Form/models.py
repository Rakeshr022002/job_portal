from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class staff_applied_job (models.Model):
    fullname=models.CharField(null=True)
    email=models.EmailField(null=True)
    phone_no=models.CharField(null=True)
    gender=models.CharField(null=True)
    dob=models.CharField(null=True)
    address=models.CharField(null=True)
    Education=models.CharField(null=True)
    job_role=models.CharField(null=True)
    experience=models.CharField(null=True)
    resume=models.FileField(null=True,upload_to='staff_resume/')
    institute_reference=models.CharField(null=True)
    staff_reference=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    
class institute_hire_staff(models.Model):
    institute_name=models.CharField(null=True)
    email=models.EmailField(null=True)
    phoneo_no=models.CharField(null=True)
    address=models.CharField(null=True)
    hire_role=models.CharField(null=True)
    salary=models.CharField(null=True)
    subject=models.CharField(null=True)
    hire_staff=models.CharField(null=True)
    institute_reference=models.ForeignKey(User,on_delete=models.CASCADE)     
 