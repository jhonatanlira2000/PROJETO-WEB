from django.db import models

class evento(models.Model):
    nome_do_evento = models.CharField(max_length=100) 
    quantidade_de_pessoas_prevista = models.CharField(max_length=100)
    promoções = models.CharField(max_length=100) 
     
    def strg (self):
        return self.nome