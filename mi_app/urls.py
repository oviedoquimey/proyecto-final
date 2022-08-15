from django.contrib import admin
from django.urls import path, include
from mi_app.views import (formulario_curso, mostrar_index, saludar_a, 
        saludo_personalizado, listar_cursos, listar_estudiantes, listar_profesor,fechas_entregable, formulario_curso, formulario_busqueda)
from mi_app import views


urlpatterns = [
    path('mi-pagina/', mostrar_index),
    path('saludar-persona/<nombre>', saludar_a),
    path('saludo/personalizado/', saludo_personalizado),
    path('listar-cursos/', listar_cursos),
    path('listar-estudiantes/', listar_estudiantes),
    path('listar-profesor/', listar_profesor),
    path('fecha-entrega/', fechas_entregable),
    path('formulario/', formulario_curso),
    path('buscar/', formulario_busqueda),
    #path('login',views.login_request, name = 'Login'),
    #path('register', views.register, name = 'Register'),
    path('accounts/', include('django.contrib.auth.urls')),
]