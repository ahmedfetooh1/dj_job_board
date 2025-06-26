from django.contrib import admin
from django.urls import path 
from . import views , api


app_name = 'job'
urlpatterns = [
    path('',views.job_list,name='job_list'),
    path('add_job',views.add_job,name='add_job'),
    path('<str:slug>',views.job_detail,name='job_detial'),
    path('api/list',api.job_list_api,name='api'),

]
