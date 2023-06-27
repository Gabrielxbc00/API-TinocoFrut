from django.db import models
from produtos.models import Produto

class Estoque(models.Model):
    setor = models.CharField(max_length=100)
    corredor = models.CharField(max_length=100)
    prateleira = models.CharField(max_length=100)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.setor} - {self.corredor} - {self.prateleira} - {self.produto}"
