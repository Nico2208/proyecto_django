from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

#views.py contiene toda la logica del negocio.

#Todo bien


def saludo (request):
    return HttpResponse("Hola a todos!")


#Request es un objeto que recibe las peticiones del usuario. Tiene informacion respecto al tipo de peticion que es.
#HttpResponse me permite devolver respuestas desde el servidor     

def saludo_modificado( request, edad ):
    documento = "<html><body><h2>Hola tenes %s anios"%(edad)
    return HttpResponse(documento)    
