from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({
                "status": True,
                "message": "Login berhasil",
                "username": username
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Username atau password salah"
            }, status=401)
    return JsonResponse({"status": False, "message": "Method not allowed"}, status=405)

