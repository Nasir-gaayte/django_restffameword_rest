from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "hi that me nasir with my first API response!!!!1"})