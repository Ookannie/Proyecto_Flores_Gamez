from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
from . import users_service

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

        # Enviar los datos a Flask
        response = users_service.create_user(user_data)

        if response.status_code == 201:
            # Éxito: redirigir a una página de éxito o realizar alguna otra acción
            return redirect('dashboard')
        else:
            # Manejar el caso de error
            return render(request, "register.html", {"error_message": "Error al enviar el registro"})


    return render(request, "register.html")


