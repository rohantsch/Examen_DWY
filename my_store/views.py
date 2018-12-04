from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Usuario

# Create your views here.

#importar user
from django.contrib.auth.models import User
#sistema de autenticación 
from django.contrib.auth import authenticate,logout, login as auth_login
from django.contrib.auth.decorators import login_required

def index(request):
    usuario = request.session.get('usuario',None)
    return render(request, 'index.html',{'usuario':usuario})

def registrar(request):
    return render(request, 'registrar.html')

<<<<<<< HEAD
def login(request):
    email = request.POST.get('email','')
    contrasenia = request.POST.get('contrasenia','')

    usuario = Usuario.objects.filter(email=email)

    if len(usuario) > 0:
        if usuario[0].contrasenia == contrasenia :
            #auth_login(request, user)
            request.session['usuario'] = usuario[0].nombre
            request.session['id'] = usuario[0].id
            return redirect('index')
        else:
            return redirect('index',{'mensaje':'Las credenciales son incorrectas.'})
    else:
        return redirect('index',{'mensaje':'No existe el Usuario.'})

def cargar(request):
    return redirect('index')
=======
def home(request):
    return render(request, 'home.html')
>>>>>>> master
