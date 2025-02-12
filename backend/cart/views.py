from django.http import JsonResponse
def cart_detail(request):
    return JsonResponse({'message': 'Cart details will appear here.'})
