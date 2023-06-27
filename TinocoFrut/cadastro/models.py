from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    TIPO_CHOICES = [
        ('cliente', 'Cliente'),
        ('funcionario', 'Funcionário'),
        ('gerente', 'Gerente'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='cadastro_user_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='cadastro_user_set',
        related_query_name='user',
    )

    def __str__(self):
        return str(self.username)
