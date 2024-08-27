from django.contrib import admin
from .models import Curso, Interesse

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'ano_conclusao')

@admin.register(Interesse)
class InteresseAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
