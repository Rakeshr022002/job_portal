from django.urls import path,include
from .views import *

urlpatterns = [
    path('',Home,name='home_page'),
    path('staff_info',staff_info,name='staff_info'),
    path('staff_view_form',staff_info_view,name='staff_view'),
    path('staff_info/update/<int:id>/',staff_update,name='update_staff'),
    path('staff_info/delete/<int:id>/',staff_delete,name='delete_staff'),
    path('job_post',post_job,name='post_job'),
    path('job_list',job_list,name='job_list'),
    path('job_post/update/<int:id>/',job_update,name='job_update'),
    path('job_post/delete/<int:id>/',job_delete,name='job_delete'),
    path('institute_overview/<int:id>/',include('Application_Form.urls'),name='institute_overview'),
    path('applied_job',include('Application_Form.urls'),name='applied_job'),
    ]