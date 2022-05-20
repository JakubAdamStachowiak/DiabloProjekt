import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output


Ua = 0.1125  # kW/m^2C
C = 4.187   # kj/kgC
P = 1.087   # kg/m^3
V = 0.063   # m^3


app = Dash(__name__)

fig = go.Figure()

app.layout = html.Div([
    dcc.Graph(id='graph'),
    html.H4(children=['Ghv']),
    dcc.Input(id="input1", type="number", placeholder="",),
    html.H4(children=['Gvi']),
    dcc.Input(id="input2", type="number", placeholder="",),
    html.H4(children=['Gc']),
    dcc.Input(id="input3", type="number", placeholder="",),
    html.H4(children=['Gp']),
    dcc.Input(id="input4", type="number", placeholder="",),
    html.H4(children=['PB']),
    dcc.Input(id="input5", type="number", placeholder="",),
    html.H4(children=['Ti']),
    dcc.Input(id="input6", type="number", placeholder="",),
    html.H4(children=['Td']),
    dcc.Input(id="input7", type="number", placeholder="",)
])



@app.callback(Output('graph', 'figure'), Input('input1', 'value'))
def update_figure():
    figure = {
        'data': [
            go.Scatter(
                x=12,
                y=13,
            )
        ]}
    return figure

app.run_server(debug=True)