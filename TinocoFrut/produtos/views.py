from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Produto

@csrf_exempt
def cadastrar_produto(request):
    if request.method == 'POST':
        identificador = request.POST.get('identificador')
        quantidade_estoque = request.POST.get('quantidade_estoque')
        descricao = request.POST.get('descricao')
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        categoria = request.POST.get('categoria')
        tipo = request.POST.get('tipo')

        produto = Produto(identificador=identificador, quantidade_estoque=quantidade_estoque, descricao=descricao,
                          nome=nome, preco=preco, categoria=categoria, tipo=tipo)
        produto.save()

        return JsonResponse({'message': 'Produto cadastrado com sucesso'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
