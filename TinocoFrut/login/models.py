from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    # Outros campos que você possa precisar

    def __str__(self):
        return str(self.username)
