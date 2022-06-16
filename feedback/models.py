from django.db import models

class feedback(models.Model):
    email = models.CharField(max_length=100) 
    código_de_compra = models.CharField(max_length=100)
    deixe_sua_avaliação = models.CharField(max_length=100) 

    def strg (self):
        return self. n_de_cadastro