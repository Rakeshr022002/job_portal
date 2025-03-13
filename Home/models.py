from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Staff_data(models.Model):
    name = models.CharField(null=True)
    email = models.EmailField(null=True)
    mobile_no = models.CharField(null=True)
    date_of_birth = models.CharField(null=True)
    gender = models.CharField(null=True)
    Education = models.CharField(null=True)
    country = models.CharField(null=True)
    state = models.CharField(null=True)
    search_role = models.CharField(null=True)
    experience = models.CharField(null=True)
    remote = models.CharField(null=True)
    Staff_img = models.ImageField(null=True,upload_to='staff_images/')
    staff_reference=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    
    

class Institute_data(models.Model):
    name = models.CharField(max_length=300,null=True)
    email = models.EmailField(null=True)
    website = models.CharField(null=True)
    department = models.CharField(null=True)
    job_role = models.CharField(null=True)    
    job_type = models.CharField(null=True)
    salary = models.CharField(null=True)
    number_of_position = models.CharField(null=True)
    qulification = models.CharField(null=True)
    experience = models.CharField(null=True)
    job_description = models.CharField(null=True)
    address = models.CharField(null=True)
    last_apply_data = models.CharField(null=True)
    interview_mode = models.CharField(null=True)
    institute_img = models.ImageField(null=True,default='Image Currently Unavailable',upload_to='institute_images/')
    institute_reference = models.ForeignKey(User,on_delete=models.CASCADE)
    
    