from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime

def saludo(request):

    fechar_hora_ahora = datetime.now()
    return HttpResponse(f"Bienvenidos! Que tal? Tu horario actual es {fechar_hora_ahora} ")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola! como estás {nombre.capitalize()}?")

