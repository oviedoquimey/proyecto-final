from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from mi_app.models import Curso, Entregable, Estudiante, Profesor

def saludo(request):

    fechar_hora_ahora = datetime.now()
    return HttpResponse(f"Bienvenidos! Que tal? Tu horario actual es {fechar_hora_ahora} ")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola! como estás {nombre.capitalize()}?")


def saludo_personalizado(request):
    pass

def mostrar_index(request):
    return render(request, "mi_app/index.html", {})

def listar_cursos(request): #vista
    context = {}
    context["cursos"] = Curso.objects.all() #modelo
    return render(request, "mi_app/lista_cursos.html", context) #template

def listar_estudiantes(request):
    context = {}
    context["estudiantes"] = Estudiante.objects.all()
    return render(request, "mi_app/lista_estudiantes.html", context)

def listar_profesor(request):
    context = {}
    context["profesores"] = Profesor.objects.all()
    return render(request, "mi_app/lista_profesor.html", context)

def fechas_entregable(request):
    context = {}
    context["entregables"] = Entregable.objects.all()
    return render(request, "mi_app/fecha_entregable.html", context)
