from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.urls import reverse

# Create your views here.

#views.py contiene toda la logica del negocio.

#Todo bien

def index( request ):
    return HttpResponse( f"""
        <h1>Hola mundo Django</h1>
    """ )

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

def curso(request, nombre_categoria):
    return HttpResponse( f'{ nombre_categoria }' ) 


def mostrar_proyecto(request, anio):
    return HttpResponse( f'{anio}' )


def quienes_somos( request ):
    #return redirect("saludo_modificado")
    return redirect( reverse( "saludar", kwargs={ "nombre": "Nicolas" } ) )
