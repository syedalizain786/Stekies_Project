from django.http import JsonResponse

def custom_404(request, exception=None):
    return JsonResponse({'error': 'Page not found'}, status=404)