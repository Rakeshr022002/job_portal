from django.urls import path,include
from .views import *

urlpatterns = [
  path('',Intro,name='intro_page'),
  path('Register',include('Register.urls')),
  ]
