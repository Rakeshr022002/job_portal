from django import forms
from django.contrib.auth import authenticate

class StaffLogin(forms.Form):
    username=forms.CharField(required=True,error_messages={'required':'Enetr username...'})
    password=forms.CharField(required=True,error_messages={'required':'Enetr password...'})
    
    
    def clean(self):
        
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        
        if username and password:
            user = authenticate(username = username ,password = password)
            
            if user is None or user.is_staff == False:
                 raise forms.ValidationError("*Invalid username and password ")
             
             
class InstituteLogin(forms.Form):
    username=forms.CharField(required=True,error_messages={'required':'Enetr username...'})
    password=forms.CharField(required=True,error_messages={'required':'Enetr password...'})
    
    
    def clean(self):
        
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        
        if username and password:
            user = authenticate(username = username ,password = password)
            
            if user is None or user.is_staff == True:
                 raise forms.ValidationError("*Invalid username and password ")             
             
         