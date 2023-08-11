from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("holaaaaaaaa")

def dashboard(request):
    context = {
 
    }
    return render(request, "dashboard.html", context)