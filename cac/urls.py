from django.urls import path

from . import views

urlpatterns = [
    path("hola/", views.saludo), 
    path("saludo/<int:edad>", views.saludo_modificado)
]

