from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Usuario, Lista, Tienda, Producto
from django.http import JsonResponse
from django.db.models import Sum

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from social_django.models import UserSocialAuth


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
            data = { 
                'mensaje': 'Usuario registrado!', 
                'type' : 'success', 
                'tittle': 'Registro Usuario',
            } 
            return JsonResponse(data,safe=False)
        else:
            data = { 
                'mensaje': 'El usuario ingresado ya esta registrado.', 
                'type' : 'warning', 
                'tittle': 'Registro Usuario',
            } 
            return JsonResponse(data,safe=False)
    else:
        data = { 
                'mensaje': 'Las contraseñas no coinciden', 
                'type' : 'error', 
                'tittle': 'Registro Usuario',
            } 
        return JsonResponse(data,safe=False)

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


def cerrar_lista(request, id):

    lista = Lista.objects.get(pk=id)
    lista.estado = False
    lista.save()

    data = { 
        'mensaje': 'Lista cerrada!', 
        'type' : 'success', 
        'tittle': 'Editar lista'
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

def aprobar_tienda(request, id):

    tienda = Tienda.objects.get(pk=id)
    tienda.estado = True
    tienda.save()

    data = { 
        'mensaje': 'Lista aprobada!', 
        'type' : 'success', 
        'tittle': 'Aprobar tienda'
    } 
        
    return JsonResponse(data)
    
def tienda(request):
    usuario = request.session.get('usuario',None)
    tiendas = Tienda.objects.all()
    cantidad = len(tiendas)
    return render(request, 'tienda.html',{'usuario':usuario, 'tiendas':tiendas, 'cantidad':cantidad})

def cerrar_session(request):
    user = request.user
    if user is None:
        usuario = request.session.get('usuario',None)
        if usuario is None:
            return redirect('home')
        else:
            del request.session['usuario']
            return redirect('index')
    else:
        auth_logout(request)
        return redirect('index')

def producto(request, id):
    usuario = request.session.get('usuario',None)
    producto = Producto.objects.filter(lista_id = id)
    lista = Lista.objects.get(pk=id)
    tiendas = Tienda.objects.all().filter(estado = True)
    cantidad = len(producto)
    return render(request, 'producto.html',{'usuario':usuario, 'cantidad':cantidad, 'productos':producto, 'lista':lista, 'tiendas':tiendas})

def crear_producto(request, id):

    nombre = request.POST.get('nombre','')
    precioPresupuesto = request.POST.get('precioPresupuesto','')
    precioReal = request.POST.get('precioReal','')
    observacion = request.POST.get('observacion','')
    comprado = request.POST.get('comprado','')
    tiendax = request.POST.get('tienda','')

    lista = Lista.objects.get(pk=id)
    tienda = Tienda.objects.get(nombre=tiendax)
    producto = Producto.objects.filter(nombre=nombre)

    if len(producto) == 0:  
        producto = Producto(nombre=nombre, precioPresupuesto=precioPresupuesto, precioReal=precioReal, observacion=observacion, comprado=comprado, tienda=tienda, lista=lista)
        producto.save()
        actualizarLista(producto.lista.id)
        data = {
            'mensaje': 'Producto creado, exitosamente!',
            'type' : 'success',
            'tittle': 'Registro producto!',
            'nombre': producto.nombre,
            'precioPresupuesto': producto.precioPresupuesto,
            'precioReal': producto.precioReal,
            'observacion': producto.observacion,
            'comprado': producto.comprado,
            'tienda': tienda.nombre,
        }
        return JsonResponse(data, safe=False)
    else:
        data = {
            'mensaje': 'El producto ya existe!',
            'type' : 'error',
            'tittle': 'Registro producto!'
        }
        return JsonResponse(data,safe=False) 

def editar_producto(request, id):
    row_number = request.POST.get('hidden_row_number','')

    nombre = request.POST.get('nombre2','')
    precioPresupuesto = request.POST.get('precioPresupuesto2','')
    precioReal = request.POST.get('precioReal2','')
    observacion = request.POST.get('observacion2','')
    comprado = request.POST.get('comprado2','')
    tiendax = request.POST.get('tienda2','')

    print(nombre)
    print(tiendax)

    producto = Producto.objects.get(pk=id)
    tienda = Tienda.objects.get(nombre=tiendax)

    producto.nombre = nombre
    producto.precioPresupuesto = precioPresupuesto
    producto.precioReal = precioReal
    producto.observacion = observacion
    producto.comprado = comprado
    producto.tienda = tienda
    
    producto.save()

    print(producto.nombre)    
    actualizarLista(producto.lista.id)
    data = {
        'mensaje': 'Producto editado, exitosamente!',
        'type' : 'success',
        'tittle': 'Edita producto',
        'nombre': producto.nombre,
        'precioPresupuesto': producto.precioPresupuesto,
        'precioReal': producto.precioReal,
        'observacion': producto.observacion,
        'comprado': producto.comprado,
        'tienda': tienda.nombre,
        'row_number': row_number
    }
    return JsonResponse(data,safe=False)

def totalProductos(id):
    productos = Producto.objects.all().filter(lista_id = id)    
    return productos.count()

def totalProductosComprados(id):
    productos = Producto.objects.all().filter(lista_id=id, comprado=True)    
    return productos.count()

def costoTotalProductos(id):
    producto = Producto.objects.filter(lista_id=id)
    total = 0
    for element in producto:
        total = total + element.precioPresupuesto
    print(total)
    return total

def costoRealProductos(id):
    producto = Producto.objects.filter(lista_id=id)
    total = 0
    for element in producto:
        total = total + element.precioReal
    print(total)
    return total

def actualizarLista(id):
    print("LISTA --------->")
    
    lista = Lista.objects.get(pk=id)
    lista.totalPresupuesto = totalProductos(id)
    lista.totalProductosComprados = totalProductosComprados(id)
    lista.costoTotalPresupuesto = costoTotalProductos(id)
    lista.costoTotalReal = costoRealProductos(id)

    lista.save()
    return True