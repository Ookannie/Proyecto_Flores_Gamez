from django.shortcuts import render
from django.http import HttpResponse
import plotly.graph_objs as go
import plotly.offline as opy
from django.shortcuts import render
import plotly.express as px
import numpy as np
import pandas as pd

def index(request):
    return HttpResponse("holaaaaaaaa")

def dashboard(request):
    # Datos simulados de pulsaciones por minuto
    dates = pd.date_range(start="2023-01-01", periods=100, freq='D')
    bpm = np.random.randint(50, 110, size=(100,))
    df = pd.DataFrame({"date": dates, "bpm": bpm})

    # Gráfica principal de pulsaciones
    fig_bpm = px.line(df, x='date', y="bpm", title="Pulsaciones por minuto a lo largo del tiempo")
    plot_bpm_html = fig_bpm.to_html(full_html=False, default_height=500)

    # Gráfica de taquicardia
    taquicardias = df[df['bpm'] > 100]
    fig_taq = px.scatter(taquicardias, x='date', y='bpm',  color_discrete_sequence=['red'])
    plot_taq_html = fig_taq.to_html(full_html=False, default_height=300)

    # Gráfica de bradicardia
    bradicardias = df[df['bpm'] < 60]
    fig_bra = px.scatter(bradicardias, x='date', y='bpm',  color_discrete_sequence=['blue'])
    plot_bra_html = fig_bra.to_html(full_html=False, default_height=300)

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

    return render(request, 'dashboard.html', context)

