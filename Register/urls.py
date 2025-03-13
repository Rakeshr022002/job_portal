from django.urls import path,include
from .views import *

urlpatterns = [
    path('staffregister',Staff_Register,name='staff_register'),
    path('institute',Institute_Register,name='institute_register'),
    path('Login',include('Login.urls'))
    ]