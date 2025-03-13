from django.urls import path
from .views import *

urlpatterns = [
    path('StaffLogin',stafflogin,name='staff_login'),
    path('instituteLogin',institutelogin,name='institute_login'),
    path('logout',logoutuser,name='logout_user')
]