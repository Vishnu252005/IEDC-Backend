from django.http import JsonResponse
from .models import MissionVisionObjective, Startup, Event, GoverningBodyMember
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist

def success_response(data, message="Success", status=200):
    return JsonResponse({"status": "success", "message": message, "data": data}, status=status)

def error_response(message="Error", status=400):
    return JsonResponse({"status": "error", "message": message}, status=status)

@require_http_methods(["GET"])
def mission_vision_objectives_view(request):
    try:
        data = MissionVisionObjective.objects.values().first()
        if data:
            return success_response(data, "Mission, Vision, and Objectives fetched successfully.")
        else:
            return error_response("No data found.", 404)
    except Exception as e:
        return error_response(str(e), 500)

@require_http_methods(["GET"])
def startups_view(request):
    try:
        data = list(Startup.objects.values())
        if data:
            return success_response(data, "Startups fetched successfully.")
        else:
            return error_response("No startups found.", 404)
    except Exception as e:
        return error_response(str(e), 500)

@require_http_methods(["GET"])
def events_view(request):
    try:
        data = list(Event.objects.values('title', 'description', 'date', 'photos'))
        if data:
            return success_response(data, "Events fetched successfully.")
        else:
            return error_response("No events found.", 404)
    except Exception as e:
        return error_response(str(e), 500)

@require_http_methods(["GET"])
def governing_body_members_view(request):
    try:
        data = list(GoverningBodyMember.objects.values('name', 'position', 'photo', 'email'))
        if data:
            return success_response(data, "Governing body members fetched successfully.")
        else:
            return error_response("No governing body members found.", 404)
    except Exception as e:
        return error_response(str(e), 500)
