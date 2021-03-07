from django.shortcuts import render,HttpResponse             
from django.conf import settings     
from galeria_imagenes.models import Album,Post
# Create your views here.

def  add_picture(request,name):         
    if request.method == "POST":              
        post=Post()          
        album=Album()       
        post.titulo=request.POST["nombre"]   
        post.contenido= request.POST["nombredelacaja"]          
        album.name=request.POST.get("nombre_album")            
        print(album.name)
        post.album.set(album.name )    
        post.imagen=request.FILES["imagen"]   
        name=request.user.username

    return render(request,"agregar_imagen.html")