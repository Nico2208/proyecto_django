from django.urls import path

from . import views

urlpatterns = [
    path("hola/", views.saludo), 
    path("saludo/<str:nombre>/<int:edad>", views.saludo_modificado),
    path("saludar/<str:nombre>", views.saludar, name="saludar"), #Agrego un alias al path
    path("saludar/", views.saludar),
    path("cursos/detalle/<slug:nombre_curso>/", views.cursos_detalle, name='cursos_detalle')
]

