from django.contrib import admin
from django.urls import path
from mi_app.views import (mostrar_index, saludar_a, 
        saludo_personalizado, listar_cursos, listar_estudiantes, listar_profesor,fechas_entregable)

urlpatterns = [
    path('mi-pagina/', mostrar_index),
    path('saludar-persona/<nombre>', saludar_a),
    path('saludo/personalizado/', saludo_personalizado),
    path('listar-cursos/', listar_cursos),
    path('listar-estudiantes/', listar_estudiantes),
    path('listar-profesor/', listar_profesor),
    path('fecha-entrega/', fechas_entregable)
]