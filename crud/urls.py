from django.contrib import admin
from django.urls import path
from crud import views
urlpatterns = [
               
             
       
    path('welcome/<name>/add_picture',views.add_picture),           
   
]