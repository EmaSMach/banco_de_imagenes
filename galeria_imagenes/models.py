from django.db import models   
from django.contrib.auth.models import User

# Create your models here.       
class Album(models.Model):   
    nombre=models.CharField(max_length=50)  
    created=models.DateTimeField(auto_now_add=True)   
    updated=models.DateTimeField(auto_now_add=True)      
    class Meta:  
        verbose_name="album"   
        verbose_name_plural="albums"    
    def __str__(self):  
        return self.nombre    

class Post(models.Model):     
    titulo=models.CharField(max_length= 50)       
 
    contenido=models.CharField(max_length=100,blank=True,null=True)      
    imagen=models.ImageField(upload_to="media")    
         
    album=models.ManyToManyField(Album)  
    updated=models.DateTimeField(auto_now_add=True)    
    created=models.DateTimeField(auto_now_add=True)     
    class Meta:   
        verbose_name="post"    
        verbose_name_plural="posts"    
    def __str__(self):     
        return self.titulo    