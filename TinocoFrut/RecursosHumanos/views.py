from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def cadastrar_funcionario(request):
    if request.method == 'POST':
        return JsonResponse({'message': 'Funcionário cadastrado com sucesso'})
    else:   
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def registrar_ponto(request):
    if request.method == 'POST':
        return JsonResponse({'message': 'Ponto registrado com sucesso'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
