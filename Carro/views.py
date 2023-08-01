from django.shortcuts import render, redirect
from .carro import Carro
from Tienda.models import Producto

# Create your views here.

def agregar_producto(request, producto_id):
    carrito = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar_producto(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carro(request)
    carrito.limpiar_carro()
    return redirect("Tienda")
