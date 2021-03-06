from django.contrib import admin
from django.urls import path
from galeria_imagenes import views
urlpatterns = [
               
    path('welcome/<name>',views.welcome),          
       
    path('logout',views.logout),           
   
]