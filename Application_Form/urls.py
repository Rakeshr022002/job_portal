from django.urls import path
from .views import*

urlpatterns=[
    # --------------------institute---------------------------------
    path('institute_overview',institute_overview,name='institute_overview'),
    path('institute_application',institute_application,name='institute_application'),
    path('applied_job',applied_job,name='applied_job'),
    path('applied_staff_overview/<int:id>/',applied_staff,name='applied_staff'),
    path('delte_applid_staff/<int:id>/',delete_applied_staff,name='delete_applied_staff'),
    # -------------------------staff-------------------------------
    
    path('staff_overview/<int:id>/',staff_overview,name='staff_overview'),
    path('hire_mail',hire_mail,name='hire_mail'),
    path('hired_job_view',hired_job_view,name='hired_job_view'),
    path('hired_job_see/<int:id>/',hired_job_see,name='hired_job_see'),
    path('hired_job_delete/<int:id>/',hired_job_delete,name='hired_job_delete')
]