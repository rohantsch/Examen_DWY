from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Usuario, Lista
from django.core import serializers
from .models import Tienda

# Create your views here.

#importar user
from django.contrib.auth.models import User
#sistema de autenticación 
from django.contrib.auth import authenticate,logout, login as auth_login
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def registrar(request):
    return render(request, 'registrar.html')

def login(request):
    email = request.POST.get('email','')
    contrasenia = request.POST.get('contrasenia','')

    usuario = Usuario.objects.filter(email=email)

    if len(usuario) > 0:
        if usuario[0].contrasenia == contrasenia :
            #auth_login(request, user)
            request.session['usuario'] = usuario[0].nombre
            request.session['id'] = usuario[0].id
            return redirect('home')
        else:
            return redirect('index',{'mensaje':'Las credenciales son incorrectas.'})
    else:
        return redirect('index',{'mensaje':'No existe el Usuario.'})

def cargar(request):
    return redirect('home')

def home(request):
    usuario = request.session.get('usuario',None)
    return render(request, 'home.html',{'usuario':usuario})

def crear_usuario(request):
    nombre = request.POST.get('nombre','')
    email = request.POST.get('email','')
    contrasenia = request.POST.get('contrasenia','')
    contrasenia2 = request.POST.get('confirm_contrasenia','')
    
    if contrasenia == contrasenia2:
        usuario = Usuario.objects.filter(email=email)
        if len(usuario) == 0:  
            usuario = Usuario(nombre=nombre, email=email, contrasenia= contrasenia)
            usuario.save()
            return redirect('index')
        else:
            return redirect('index',{'mensaje':'El usuario ingresado ya esta registrado.'})
    else:
        return redirect('index',{'mensaje':'Las contraseñas no coinciden'})

def crear_lista(request):

    nombre = request.POST.get('nombre','')

    id = request.session.get('id',None)
    usuario = Usuario.objects.get(pk=id)

    lista = Lista.objects.filter(nombre=nombre, usuario=usuario)

    if len(lista) == 0:  
        lista = Lista(usuario=usuario, nombre= nombre, totalPresupuesto = 0, totalProductosComprados= 0, costoTotalPresupuesto= 0, costoTotalReal=0, estado=False)
        lista.save()
        return serializers.serialize('json', lista)
    else:
        return serializers.serialize('json', lista)
    return False

def crear_tienda(request):

    nombre = request.POST.get('nombre','')
    nombreSucursal = request.POST.get('nombreSucursal','')
    direccion = request.POST.get('direccion','')
    region = request.POST.get('region','')
    comuna = request.POST.get('comuna','')

    tienda = Tienda.objects.filter(nombre=nombre)

    if len(lista) == 0:  
        tienda = Tienda(nombre=nombre, nombreSucursal=nombreSucursal, direccion=direccion, region=region, comuna=comuna, estado=False)
        tienda.save()
        return redirect('tienda')
    else:
        return redirect('tienda',{'mensaje':'La tiena ya existe'})
    
def tienda(request):
    usuario = request.session.get('usuario',None)
    tiendas = Tienda.objects.all()
    cantidad = len(tiendas)
    return render(request, 'tienda.html',{'usuario':usuario, 'tiendas':tiendas, 'cantidad':cantidad})
