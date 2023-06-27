from django.db import models

class Compra(models.Model):
    fornecedor = models.CharField(max_length=100)
    data = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    # Outros campos relevantes para a compra

    def __str__(self):
        return f"Compra {self.pk}"

class Venda(models.Model):
    cliente = models.CharField(max_length=100)
    data = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    # Outros campos relevantes para a venda

    def __str__(self):
        return f"Venda {self.pk}"
