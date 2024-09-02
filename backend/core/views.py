from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from core.models import RadioactiveMaterial


@require_http_methods(["GET"])
def calculate_activity(request):
    try:
        radiation_level = float(request.GET.get('radiation_level', 0))
        altitude = float(request.GET.get('altitude', 0))
    except ValueError:
        return JsonResponse({'error': 'Invalid input'}, status=400)

    radioactive_materials = RadioactiveMaterial.objects.all()
    response = []
    for rm in radioactive_materials:
        activity = (radiation_level * altitude * altitude) / rm.constant
        response.append({'material': rm.name, 'constant': rm.constant, 'activity': activity})

    return JsonResponse(response, safe=False)
