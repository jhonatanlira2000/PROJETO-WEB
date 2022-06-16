from django.db import models

class rastreio(models.Model):
    endereço = models.CharField(max_length=100) 
    remetente = models.CharField(max_length=100)
    codigo_de_rastreio = models.CharField(max_length=100) 
     
    def strg (self):
        return self.nome