from django.db import models
class produtos(models.Model):
    modelo = models.CharField(max_length=100) 
    código = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100) 
    preço = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)

    def strg (self):
        return self.modelo
