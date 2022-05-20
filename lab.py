import plotly.graph_objects as go
from math import sqrt
import numpy as np
from dash import Dash, dcc, html, Input, Output


app = Dash(__name__)

fig = go.Figure()


A = 1.5
Beta = 0.035
h_min = 0.0
h_max = 5.0

t_sim = 1500

kp = 0.025
Ti = 2.5
Td = 0.75
Tp = 0.1
u_min = 0.0
u_max = 10.0

Qd_min = 0.0
Qd_max = 0.05

t = [0.0, ]
e = [0.0, ]
u_PID = [0.0, ]
u = [0.0, ]

Qd = [0.0, ]
Qo = [0.0, ]
h = [0.0, ]

N = int(t_sim/ Tp) +1
h_zad = [1.5, ]

x = np.arange(0, 3600, 1)

slider = dcc.Slider(
        0, 100, 1,
        value=1,
        id='slider',
    )

app.layout = html.Div([
    dcc.Graph(id='graph'), slider, dcc.Graph(id='graph1')])


@app.callback(Output('graph', 'figure'), Output('graph1', 'figure'), Input('slider', 'value'))
def update_figure(value):
    h = [0.0, ]
    for n in range(1, N):
        t.append(n * Tp)
        e.append(h_zad[-1] - h[-1])
        u_PID.append(kp * (e[-1] + Tp * sum(e) / Ti + Td * (e[-1]) - e[-2] / Tp))
        u.append(max(u_min, min(u_max, u_PID[-1])))
        Qd.append((Qd_max - Qd_min) * (u[-1] - u_min) / (u_max - u_min) + Qd_min)
        h.append(max(h_min, min(h_max, Tp * (Qd[-1] - Qo[-1]) / A + h[-1])))
        h_zad.append(h_zad[-1])
        Qo.append(Beta * h[-1] ** 0.5)
    figure = {
        'data': [
            go.Scatter(
                x=t,
                y=h,
            )
        ]
        ,
    }
    return figure



app.run_server(debug=True)
