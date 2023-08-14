from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola mundo")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

