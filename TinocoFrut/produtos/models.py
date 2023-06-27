from django.db import models

class Produto(models.Model):
    identificador = models.PositiveIntegerField()
    quantidade_estoque = models.PositiveIntegerField()
    descricao = models.TextField()
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.nome)
