from django.shortcuts import render,redirect          
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm          
from django.contrib.auth import login as do_login          
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def welcome(request,name):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:           
        name=name=request.user.username
        return render(request, "welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')        


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')