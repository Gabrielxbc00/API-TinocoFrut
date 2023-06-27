from django.urls import path
from . import views

urlpatterns = [
    path('comprar/', views.comprar, name='comprar'),
    path('vender/', views.vender, name='vender'),
    path('fiscal/', views.fiscal, name='fiscal'),
    path('relatorio/compra/', views.relatorio_compra, name='relatorio_compra'),
    path('relatorio/vendas/', views.relatorio_vendas, name='relatorio_vendas'),
]
