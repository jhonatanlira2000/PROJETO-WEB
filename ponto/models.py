from django.db import models

class ponto(models.Model):
    nome_do_funcionario = models.CharField(max_length=100) 
    hora_de_entrada = models.CharField(max_length=100)
    hora_da_saida = models.CharField(max_length=100) 
    
    def strg (self):
        return self.nome