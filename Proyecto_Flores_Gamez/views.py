from django.http import HttpResponse
from django.shortcuts import render
import json

def saludo(request):
    return HttpResponse("Hola mundo")

def login(request):
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeated_password')
        
        # Obtener los datos de los thresholds agregados dinámicamente
        threshold_names = request.POST.getlist('threshold_name')
        threshold_highs = request.POST.getlist('threshold_high')
        threshold_lows = request.POST.getlist('threshold_low')
        
        thresholds = []
        for name, high, low in zip(threshold_names, threshold_highs, threshold_lows):
            thresholds.append({'name': name, 'high': int(high), 'low': int(low)})
        
        user_data = {
            'name': f'{first_name} {last_name}',
            'age': age,
            'email': email,
            'thresholds': thresholds,
            'password' : password,
        }
        
        # Convertir el diccionario en un JSON
        user_json = json.dumps(user_data)

        # Redirigir a una página de éxito o realizar alguna otra acción
        return render(request, "register.html", {"user_json": user_json})

    return render(request, "register.html")


