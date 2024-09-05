import json

from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods

from core.models import RadioactiveMaterial, Result
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt


@require_http_methods(["GET"])
def get_materials(request):
    radioactive_materials = RadioactiveMaterial.objects.all().order_by('name')
    materials_list = [
        {
            "name": material.name,
            "constant": material.constant
        }
        for material in radioactive_materials
    ]

    return JsonResponse(materials_list, safe=False)


@require_http_methods(["POST"])
def create_material(request):
    try:
        data = json.loads(request.body)
        name = data.get("name")
        constant = data.get("constant")

        if not name or constant is None:
            return HttpResponseBadRequest("O nome e a constante são obrigatórios.")

        material = RadioactiveMaterial(name=name, constant=constant)
        material.save()

        return JsonResponse({
            "id": material.id,
            "name": material.name,
            "constant": material.constant
        }, status=201)

    except json.JSONDecodeError:
        return HttpResponseBadRequest("Formato JSON inválido.")


@require_http_methods(["GET"])
def calculate_activity(request):
    try:
        radiation_level = float(request.GET.get('radiation_level', 0))
        altitude = float(request.GET.get('altitude', 0))
    except ValueError:
        return JsonResponse({'error': 'Invalid input'}, status=400)

    radioactive_materials = RadioactiveMaterial.objects.all().order_by('name')
    response = []
    for rm in radioactive_materials:
        activity = (radiation_level * altitude * altitude) / rm.constant
        response.append({'material': rm.name, 'constant': rm.constant, 'activity': activity})

    return JsonResponse(response, safe=False)


@require_http_methods(["POST"])
def create_result(request):
    try:
        data = json.loads(request.body)
        date = data.get("date")
        radiation_level = data.get("radiation_level")
        altitude = data.get("altitude")

        if not date or radiation_level is None or altitude is None:
            return HttpResponseBadRequest("Data, nível de radiação e altitude são obrigatórios.")

        result = Result(date=date, radiation_level=radiation_level, altitude=altitude)
        result.save()

        return JsonResponse({
            "id": result.id,
            "date": result.date,
            "radiation_level": result.radiation_level,
            "altitude": result.altitude
        }, status=201)

    except json.JSONDecodeError:
        return HttpResponseBadRequest("Formato JSON inválido.")


@require_http_methods(["GET"])
def get_results(request):
    results = Result.objects.all().order_by('-date')
    results_list = [
        {
            "date": result.date,
            "radiation_level": result.radiation_level,
            "altitude": result.altitude
        }
        for result in results
    ]

    return JsonResponse(results_list, safe=False)

