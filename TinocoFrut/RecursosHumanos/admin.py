from django.contrib import admin
from .models import Setor, Cargo, Funcionario, FolhaDePonto

admin.site.register(Setor)
admin.site.register(Cargo)
admin.site.register(Funcionario)
admin.site.register(FolhaDePonto)
