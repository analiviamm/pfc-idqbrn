import json

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.http import require_http_methods

from core.models import RadioactiveMaterial, Result


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
        flight_description = data.get("flight_description")
        altitude = data.get("altitude")
        access_restrict = data.get("access_restrict")
        tireoide_monitoring = data.get("tireoide_monitoring")
        aliment_restrict = data.get("aliment_restrict")
        people_reallocation = data.get("people_reallocation")
        immediate_evacuation = data.get("immediate_evacuation")
        first_minute_contact = data.get("first_minute_contact")
        second_minute_contact = data.get("second_minute_contact")

        if not date or radiation_level is None or altitude is None:
            return HttpResponseBadRequest("Data, nível de radiação e altitude são obrigatórios.")

        result = Result(date=date, radiation_level=radiation_level, altitude=altitude,
                        flight_description=flight_description,
                        access_restrict=access_restrict, tireoide_monitoring=tireoide_monitoring,
                        aliment_restrict=aliment_restrict, people_reallocation=people_reallocation,
                        immediate_evacuation=immediate_evacuation, first_minute_contact=first_minute_contact,
                        second_minute_contact=second_minute_contact
                        )
        result.save()

        return JsonResponse({
            "id": result.id,
            "date": result.date,
            "radiation_level": result.radiation_level,
            "flight_description": result.flight_description,
            "altitude": result.altitude,
            "access_restrict": result.access_restrict,
            "tireoide_monitoring": result.tireoide_monitoring,
            "aliment_restrict": result.aliment_restrict,
            "people_reallocation": result.people_reallocation,
            "immediate_evacuation": result.immediate_evacuation,
            "first_minute_contact": result.first_minute_contact,
            "second_minute_contact": result.second_minute_contact,

        }, status=201)

    except json.JSONDecodeError:
        return HttpResponseBadRequest("Formato JSON inválido.")


@require_http_methods(["PUT"])
def edit_result(request, result_id):
    try:
        # Carrega o corpo da requisição
        data = json.loads(request.body)

        # Tenta obter o objeto Result a ser atualizado
        try:
            result = Result.objects.get(id=result_id)
        except Result.DoesNotExist:
            return HttpResponseNotFound("Resultado não encontrado.")
        print(result)
        print(data)
        # Atualiza os campos apenas se forem enviados na requisição
        result.date = data.get("date", result.date)
        result.radiation_level = data.get("radiation_level", result.radiation_level)
        result.flight_description = data.get("flight_description", result.flight_description)
        result.altitude = data.get("altitude", result.altitude)
        result.access_restrict = data.get("access_restrict", result.access_restrict)
        result.tireoide_monitoring = data.get("tireoide_monitoring", result.tireoide_monitoring)
        result.aliment_restrict = data.get("aliment_restrict", result.aliment_restrict)
        result.people_reallocation = data.get("people_reallocation", result.people_reallocation)
        result.immediate_evacuation = data.get("immediate_evacuation", result.immediate_evacuation)
        result.first_minute_contact = data.get("first_minute_contact", result.first_minute_contact)
        result.second_minute_contact = data.get("second_minute_contact", result.second_minute_contact)

        # Salva as alterações no banco de dados
        result.save()

        # Retorna os dados atualizados
        return JsonResponse({
            "id": result.id,
            "date": result.date,
            "radiation_level": result.radiation_level,
            "flight_description": result.flight_description,
            "altitude": result.altitude,
            "access_restrict": result.access_restrict,
            "tireoide_monitoring": result.tireoide_monitoring,
            "aliment_restrict": result.aliment_restrict,
            "people_reallocation": result.people_reallocation,
            "immediate_evacuation": result.immediate_evacuation,
            "first_minute_contact": result.first_minute_contact,
            "second_minute_contact": result.second_minute_contact,
        }, status=200)

    except json.JSONDecodeError:
        return HttpResponseBadRequest("Formato JSON inválido.")


@require_http_methods(["GET"])
def get_results(request):
    results = Result.objects.all().order_by('-date')
    results_list = [
        {
            "id": result.id,
            "date": result.date,
            "radiation_level": result.radiation_level,
            "altitude": result.altitude,
            "flight_description": result.flight_description,
            "access_restrict": result.access_restrict,
            "tireoide_monitoring": result.tireoide_monitoring,
            "aliment_restrict": result.aliment_restrict,
            "people_reallocation": result.people_reallocation,
            "immediate_evacuation": result.immediate_evacuation,
            "first_minute_contact": result.first_minute_contact,
            "second_minute_contact": result.second_minute_contact,

        }
        for result in results
    ]

    return JsonResponse(results_list, safe=False)


@require_http_methods(["DELETE"])
def delete_all_results(request):
    deleted_ids = []
    results = Result.objects.all()
    for result in results:
        result.delete()
        deleted_ids.append({"id": result.id})
    return JsonResponse(deleted_ids, safe=False)


@require_http_methods(["DELETE"])
def delete_result(request):
    result_id = request.GET.get('result_id')
    if not result_id:
        return JsonResponse({'error': 'result_id is required'}, status=400)

    try:
        result = Result.objects.get(id=result_id)
        result.delete()
        response = {'id_deleted': result_id}
        return JsonResponse(response)
    except Result.DoesNotExist:
        return JsonResponse({'error': 'Result not found'}, status=404)