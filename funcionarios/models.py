from django.db import models

class funcionarios(models.Model):
    nome = models.CharField(max_length=100) 
    idade = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100) 
    endereço = models.CharField(max_length=100)
    escolaridade = models.CharField(max_length=100)

    def strg (self):
        return self.nome
    