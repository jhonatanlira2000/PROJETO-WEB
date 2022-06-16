from django.db import models

class trabalhe(models.Model):
    nome = models.CharField(max_length=100) 
    experiência = models.CharField(max_length=100)
    email = models.CharField(max_length=100) 
    contato = models.CharField(max_length=100)

    def strg (self):
        return self.nome