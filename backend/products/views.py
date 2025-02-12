from django.http import JsonResponse
def product_list(request):
    return JsonResponse({'message': 'List of products will appear here.'})
