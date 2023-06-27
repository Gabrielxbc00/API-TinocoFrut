from django.db import models

class Setor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nome)

class Cargo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nome)

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    carga_horaria = models.PositiveIntegerField()
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nome)

class FolhaDePonto(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data = models.DateField()
    entrada = models.TimeField()
    saida = models.TimeField()

    def __str__(self):
        return f"Folha de Ponto - {self.funcionario} - {self.data}"
