from django.db import models

class cliente(models.Model):
    nome = models.CharField(max_length=100) 
    sexo = models.CharField(max_length=100)
    endereço_completo = models.CharField(max_length=100) 
    e_mail= models.CharField(max_length=100)
    CPF = models.CharField(max_length=100)

    def strg (self):
        return self.nome
