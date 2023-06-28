from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def comprar(request):
    if request.method == 'POST':
        return JsonResponse({'message': 'Compra realizada com sucesso'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def vender(request):
    if request.method == 'POST':
        return JsonResponse({'message': 'Venda realizada com sucesso'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def fiscal(request):
    return JsonResponse({'message': 'Aspectos fiscais atualizados'})

def relatorio_compra(request):
    return JsonResponse({'message': 'Relatório de compra gerado'})

def relatorio_vendas(request):
    return JsonResponse({'message': 'Relatório de vendas gerado'})
