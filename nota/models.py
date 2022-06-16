from django.db import models

# Create your models here.
class nota(models.Model):
    
    empresa = models.CharField(max_length=100) 
    cliente = models.CharField(max_length=100)
    N_de_vendas = models.CharField(max_length=100) 
    Nf = models.CharField(max_length=100)
    Serviços_executados = models.CharField(max_length=100)

    def strg (self):
        return self.empresa
