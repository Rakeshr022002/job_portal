from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class All_Staff_List(models.Model):
    username=models.CharField()
    email=models.EmailField()
    join_date=models.CharField()
    staff_reference=models.ForeignKey(User,on_delete=models.CASCADE) 

class All_Institute_List(models.Model):
    username=models.CharField(null=True)
    email=models.EmailField(null=True)
    join_date=models.CharField(null=True)
    institute_reference=models.ForeignKey(User,on_delete=models.CASCADE)    