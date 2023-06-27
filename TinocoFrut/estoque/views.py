from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Estoque
from produtos.models import Produto

@csrf_exempt
def adicionar_produto(request):
    if request.method == 'POST':
        setor = request.POST.get('setor')
        corredor = request.POST.get('corredor')
        prateleira = request.POST.get('prateleira')
        produto_id = request.POST.get('produto_id')

        produto = get_object_or_404(Produto, id=produto_id)

        estoque = Estoque(setor=setor, corredor=corredor, prateleira=prateleira, produto=produto)
        estoque.save()

        return JsonResponse({'message': 'Produto adicionado ao estoque com sucesso'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
