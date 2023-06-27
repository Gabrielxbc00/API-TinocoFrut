from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('registrar_ponto/', views.registrar_ponto, name='registrar_ponto'),
]
