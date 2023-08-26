from django.shortcuts import render
from django.http import HttpResponse
import plotly.graph_objs as go
import plotly.offline as opy
from django.shortcuts import render
import plotly.express as px



# Create your views here.
def index(request):
    return HttpResponse("holaaaaaaaa")

def dashboard(request):
    df = px.data.stocks()
    fig = px.line(df, x='date', y="GOOG")
    
    # Convierte el gráfico a HTML
    plot_html = fig.to_html(full_html=False, default_height=500)
    
    return render(request, 'dashboard.html', {'plot_html': plot_html})