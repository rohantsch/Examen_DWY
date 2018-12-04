from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    contrasenia = models.CharField(max_length=40)

    def __str(self):
        return "USUARIO"

class Tienda(models.Model):
    nombre = models.CharField(max_length=40)
    nombreSucursal = models.CharField(max_length=40)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    estado = models.BooleanField()
    
    def __str__(self):
        return "TIENDA"
    
class Lista(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    totalPresupuesto = models.IntegerField()
    totalProductosComprados = models.IntegerField()
    costoTotalPresupuesto = models.IntegerField()
    costoTotalReal = models.IntegerField()
    estado = models.BooleanField()
    
    def __str__(self):
        return "LISTA"

class Producto(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    precioPresupuesto = models.IntegerField()
    precioReal = models.IntegerField()
    observacion = models.CharField(max_length=100)
    comprado = models.BooleanField()
    
    def __str__(self):
        return "PRODUCTO"

