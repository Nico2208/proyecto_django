from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

#views.py contiene toda la logica del negocio.


def saludo( request ):
    return HttpResponse("Hola a todos!")

def saludo_modificado( request, edad ):
    documento = "<html><body><h2>Hola tenes %s anios"%(edad)
    return HttpResponse(documento)    
