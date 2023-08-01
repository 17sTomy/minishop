from django.shortcuts import render
from Servicios.models import Servicio

# Create your views here.

def servicios(request):
    servicios = Servicio.objects.all() # importa todos los servicios creados
    return render(request, "servicios/servicios.html", {"servicios": servicios})
