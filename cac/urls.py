from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="inicio"),
    path("hola/", views.saludo), 
    path("saludo/<str:nombre>/<int:edad>", views.saludo_modificado),
    re_path(r"^proyectos/(?P<anio>\d{4})/$", views.mostrar_proyecto, name='mostrar'),
    path("saludar/<str:nombre>", views.saludar, name="saludar"), #Agrego un alias al path
    path("saludar/", views.saludar),
    path("cursos/detalle/<slug:nombre_curso>/", views.cursos_detalle, name='cursos_detalle'),
    re_path(r"^cursos/(?P<nombre_categoria>\w{1,4})/$", views.curso, name='cursos'),
    path("quienessomos/", views.quienes_somos, name="quienes_somos"),
    path('holamundo/', views.index_saludo, name="index" ),
    path('cursos/', views.ver_proyectos, name='cursos')
]

 