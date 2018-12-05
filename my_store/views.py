from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Usuario, Lista
from django.http import JsonResponse
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
    id = request.session.get('id',None)
    listas = Lista.objects.all().filter(usuario_id=id)
    cantidad = len(listas)
    return render(request, 'home.html',{'usuario':usuario, 'listas': listas, 'cantidad':cantidad})

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
        lista = Lista(usuario=usuario, nombre= nombre, totalPresupuesto = 0, totalProductosComprados= 0, costoTotalPresupuesto= 0, costoTotalReal=0, estado=True)
        lista.save()        
        data = {
            'mensaje': 'Lista creada, exitosamente!',
            'type' : 'success',
            'id_lista': lista.id,
            'nombre_lista': lista.nombre,
            'tittle': 'Creado!'
        }
        return JsonResponse(data, safe=False)
    else:
        data = {
            'mensaje': 'Esta lista, ya ha sido creada',
            'type' : 'error',
            'tittle': 'Error!'
        }
        return JsonResponse(data,safe=False)  

def editar_lista(request, id):
    nombre = request.POST.get('editar_nombre','')
    row_number = request.POST.get('hidden_row_number','')
    
    lista = Lista.objects.get(pk=id)
    lista.nombre = nombre
    lista.save()

    data = { 
        'mensaje': 'Lista, editada!', 
        'type' : 'success', 
        'tittle': 'Editar lista',
        'id': lista.id,
        'nombre': lista.nombre,
        'totalPresupuesto' : lista.totalPresupuesto,
        'totalProductoComprados': lista.totalProductosComprados,
        'costoTotalPresupuesto': lista.costoTotalPresupuesto,
        'costoTotalReal': lista.costoTotalReal,
        'estado': lista.estado,
        'row_number': row_number
    } 
        
    return JsonResponse(data)

def crear_tienda(request):

    nombre = request.POST.get('nombre','')
    nombreSucursal = request.POST.get('nombreSucursal','')
    direccion = request.POST.get('direccion','')
    region = request.POST.get('region','')
    ciudad = request.POST.get('comuna','')

    tienda = Tienda.objects.filter(nombre=nombre)

    if len(tienda) == 0:  
        tienda = Tienda(nombre=nombre, nombreSucursal=nombreSucursal, direccion=direccion, region=region, ciudad=ciudad, estado=False)
        tienda.save()
        data = {
            'mensaje': 'Tienda creada, exitosamente!',
            'type' : 'success',
            'nombre': tienda.nombre,
            'nombreSucursal': tienda.nombreSucursal,
            'direccion': tienda.direccion,
            'region': tienda.region,
            'ciudad': tienda.ciudad,
            'estado': tienda.estado,
            'tittle': 'Creado!'
        }
        return JsonResponse(data, safe=False)
    else:
        data = {
            'mensaje': 'Esta tienda, ya existe!',
            'type' : 'error',
            'tittle': 'Error!'
        }
        return JsonResponse(data,safe=False) 

def editar_tienda(request,id):
    row_number = request.POST.get('hidden_row_number','')

    nombre = request.POST.get('nombre2','')
    nombreSucursal = request.POST.get('nombreSucursal2','')
    direccion = request.POST.get('direccion2','')
    region = request.POST.get('region2','')
    ciudad = request.POST.get('comuna2','')

    tienda = Tienda.objects.get(pk=id)

    tienda.nombre = nombre
    tienda.nombreSucursal = nombreSucursal
    tienda.direccion = direccion
    tienda.region = region  
    tienda.ciudad = ciudad
    
    tienda.save()

    data = {
        'mensaje': 'Tienda editada, exitosamente!',
        'type' : 'success',
        'tittle': 'Editar lista',
        'nombre': tienda.nombre,
        'nombreSucursal': tienda.nombreSucursal,
        'direccion': tienda.direccion,
        'region': tienda.region,
        'ciudad': tienda.ciudad,
        'estado': tienda.estado,
        'row_number': row_number
    }
    return JsonResponse(data)

    
def tienda(request):
    usuario = request.session.get('usuario',None)
    tiendas = Tienda.objects.all()
    cantidad = len(tiendas)
    return render(request, 'tienda.html',{'usuario':usuario, 'tiendas':tiendas, 'cantidad':cantidad})

def cerrar_session(request):
    del request.session['usuario']
    return redirect('index')