from django import forms
from django.contrib.auth.models import User


class StaffRegister(forms.ModelForm):
    username=forms.CharField(min_length=3,max_length=30,required=True,error_messages={'required':'Enetr username...'})
    email=forms.EmailField(required=True,error_messages={'required':'Enetr Email Address...'})
    password=forms.CharField(min_length=8,required=True,error_messages={'required':'Enetr your password...'})
    confirm_password=forms.CharField(min_length=3,required=True)
    is_staff=forms.BooleanField(required=True,error_messages={'required':'click Agree'})
    
    class Meta:
        model = User
        fields=['username','email','password','is_staff']
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')    
        confirm_password = cleaned_data.get('confirm_password')
        
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("*password does't match")   
            

class InstituteRegister(forms.ModelForm):
    username=forms.CharField(min_length=3,max_length=250,required=True,error_messages={'required':'Enter username...'})
    email=forms.EmailField(required=True,error_messages={'required':'Enter Email Address...'})
    password=forms.CharField(min_length=8,required=True,error_messages={'required':'Enter your password...'})
    confirm_password=forms.CharField(min_length=3,required=True)
    
    class Meta:
        model = User
        fields=['username','email','password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')    
        confirm_password = cleaned_data.get('confirm_password')
        
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("*password does't match")                             