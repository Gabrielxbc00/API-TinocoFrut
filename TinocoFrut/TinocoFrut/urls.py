from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', include('login.urls')),
    path('api/cadastro/', include('cadastro.urls')),
    path('api/produtos/', include('produtos.urls')),
    path('api/estoque/', include('estoque.urls')),
    path('api/financeiro/', include('financeiro.urls')),
    path('api/RecursosHumanos/', include('RecursosHumanos.urls')),
]
