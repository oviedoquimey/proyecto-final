from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from mi_app.models import Curso, Entregable, Estudiante, Profesor
from mi_app.forms import CursoBusquedaFormulario, CursoFormulario
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


@login_required

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


def formulario_curso(request):

    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid:
                informacion = mi_formulario.cleaned_data
                curso = Curso (nombre=informacion['curso'], camada=informacion['camada'])
                curso.save()
                return render(request, "AppCoder/inicio.html")
    else:
        mi_formulario = CursoFormulario()
    return render(request, "mi_app/curso_formulario.html",{"mi_formulario":mi_formulario})

def formulario_busqueda(request):
    busqueda_formulario = CursoBusquedaFormulario()
    if request.GET:
        cursos = Curso.objects.filter(nombre=busqueda_formulario["criterio"]).all()
        return render(request,"mi_app/curso_busqueda.html", {"cursos": cursos})
    
    return render(request, "mi_app/curso_busqueda.html", {"busqueda_formulario": busqueda_formulario})

#def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request. user)
                return render(request, "mi_app/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "mi_app/inicio.html", {"mensaje": "Error, datos incorrectos"})

        else:
                return render(request,"mi_app/incio.html", {"mensaje":"Error, formulario erroneo"})
    form = AuthenticationForm()
    return render(request,"mi_app/login.html", {'form':form})


#def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"mi_app/inicio.html" , {"mensaje":"Usuario Creado :)"})

    else:
        form = UserCreationForm()
        form = UserRegisterForm()

    return render(request,"mi_app/registro.html", {"form":form})




