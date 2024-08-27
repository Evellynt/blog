from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    ano_conclusao = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nome} - {self.instituicao}"

class Interesse(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo
