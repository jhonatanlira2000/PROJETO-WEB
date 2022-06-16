from django.db import models

class fornecedores(models.Model):
    n_de_cadastro = models.CharField(max_length=100) 
    CNPJ = models.CharField(max_length=100)
    endereço_completo = models.CharField(max_length=100) 
    ramo_de_atividade= models.CharField(max_length=100)
    contato = models.CharField(max_length=100)

    def strg (self):
        return self. n_de_cadastro
