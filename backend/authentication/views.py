from django.http import JsonResponse
def login_view(request):
    return JsonResponse({'message': 'Login endpoint'})

def logout_view(request):
    return JsonResponse({'message': 'Logout endpoint'})

def register_view(request):
    return JsonResponse({'message': 'Register endpoint'})
