from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.urls import reverse

from django.template import loader

# Create your views here.

#views.py contiene toda la logica del negocio.

#Todo bien

def index( request ):
    if( request.method == 'GET' ):
        titulo = "Titulo cuando accedo por el metodo GET"
    else:
        titulo = f"Titulo cuando accedo por el metodo {request.method}"
    listado_cursos = [
        {
            'nombre': 'fullstack Java',
            'descripcion': 'curso desarrollador fullstack'
        },
        {
            'nombre': 'Diseño UX/UI',
            'descripcion': 'curso diseño'
        },
        {
            'nombre': 'Big Data',
            'descripcion': 'curso analisis de datos'
        }
    ]
    return render(request, "saludo.html", {'titulo':titulo, 'listado': listado_cursos})

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

def index_saludo(request):
    return render(request, "index.html", {"nombre":"Nicolas"})

def ver_proyectos( request, anio=2022, mes=1 ):

    listado_cursos = [
        {
            'nombre': 'fullstack Java',
            'descripcion': 'curso desarrollador fullstack'
        },
        {
            'nombre': 'Diseño UX/UI',
            'descripcion': 'curso diseño'
        },
        {
            'nombre': 'Big Data',
            'descripcion': 'curso analisis de datos'
        }
    ]

    return render( request, 'cursos.html', {'cursos': listado_cursos} )

