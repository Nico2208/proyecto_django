from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

#views.py contiene toda la logica del negocio.

#Todo bien


def saludo (request):
    return HttpResponse("Hola a todos!")


#Request es un objeto que recibe las peticiones del usuario. Tiene informacion respecto al tipo de peticion que es.
#HttpResponse me permite devolver respuestas desde el servidor     

def saludo_modificado( request, nombre, edad ):
    documento = f"<html><body><h2>Hola {nombre}, tenes {edad} años"
    return HttpResponse(documento)


def saludar(request, nombre='Nico'):
    return HttpResponse(f"""
        <h1>Hola mundo Django - Un gusto {nombre}</h1>
    """)

def cursos_detalle(request, nombre_curso):
    return HttpResponse( f'{ nombre_curso }' )    
