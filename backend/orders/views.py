from django.http import JsonResponse
def order_list(request):
    return JsonResponse({'message': 'List of orders will appear here.'})
