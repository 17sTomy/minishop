from django.shortcuts import render
from .models import Producto, CategoriaProd

# Create your views here.

def tienda(request):
    productos = Producto.objects.all()
    categorias = CategoriaProd.objects.all()
    return render(request, "tienda/tienda.html", {"productos": productos, "categorias": categorias})

def productos_filtrados(request, categoria_id):
    categorias = CategoriaProd.objects.all()
    categoria_seleccionada = CategoriaProd.objects.get(id=categoria_id)
    productos_filtrados = Producto.objects.filter(categorias=categoria_seleccionada)
    return render(request, "tienda/categoria.html", {"productos_filtrados": productos_filtrados, "categorias": categorias})