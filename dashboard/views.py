from django.shortcuts import render, redirect
from django.http import HttpResponse
import plotly.graph_objs as go
import plotly.offline as opy
from django.shortcuts import render
import plotly.express as px
import numpy as np
import pandas as pd
import requests

def index(request):
    return HttpResponse("holaaaaaaaa")

def dashboard(request):
    # Datos simulados de pulsaciones por minuto
    dates = pd.date_range(start="2023-01-01", periods=100, freq='D')
    bpm = np.random.randint(50, 110, size=(100,))
    df = pd.DataFrame({"date": dates, "bpm": bpm})

    # Gráfica principal de pulsaciones
    fig_bpm = px.line(df, x='date', y="bpm")
    plot_bpm_html = fig_bpm.to_html(full_html=False, default_height=500, div_id="plot_bpm")

    # Gráfica de taquicardia
    taquicardias = df[df['bpm'] > 100]
    fig_taq = px.scatter(taquicardias, x='date', y='bpm',  color_discrete_sequence=['red'])
    plot_taq_html = fig_taq.to_html(full_html=False, default_height=300, div_id="plot_taq")

    # Gráfica de bradicardia
    bradicardias = df[df['bpm'] < 60]
    fig_bra = px.scatter(bradicardias, x='date', y='bpm',  color_discrete_sequence=['blue'])
    plot_bra_html = fig_bra.to_html(full_html=False, default_height=300, div_id="plot_bra")

    # KPIs
    min_bpm = np.min(bpm)
    max_bpm = np.max(bpm)
    avg_bpm = np.mean(bpm)
    latest_bpm = bpm[-1]

    context = {
        'plot_bpm_html': plot_bpm_html,
        'plot_taq_html': plot_taq_html,
        'plot_bra_html': plot_bra_html,
        'min_bpm': min_bpm,
        'max_bpm': max_bpm,
        'avg_bpm': avg_bpm,
        'latest_bpm': latest_bpm
    }

    if request.method == 'POST':
        intervalo = request.POST.get('intervalo')
        if intervalo:
            try:
                response = requests.post('http://localhost:5000/actualizar_intervalo', json=intervalo)
                return response
            except ValueError:
                pass
        return redirect('dashboard.html')
    else:
        return render(request, 'dashboard.html', context)   



