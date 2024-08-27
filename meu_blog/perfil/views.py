from django.shortcuts import render
from .models import Curso, Interesse

def home(request):
    cursos = Curso.objects.all()
    interesses = Interesse.objects.all()
    return render(request, 'perfil/home.html', {'cursos': cursos, 'interesses': interesses})

def sobre(request):
    return render(request, 'perfil/sobre.html')
