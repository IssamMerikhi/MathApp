# Environment used: dash1_8_0_env
import pandas as pd     #(version 1.0.0)
import plotly           #(version 4.5.0)
import plotly.express as px
import numpy as np
import dash             #(version 1.8.0)
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
import random
# print(px.data.gapminder()[:15])

app = dash.Dash(__name__)

#---------------------------------------------------------------
app.layout = html.Div([

    html.Div([
        html.H2("By maths teachers, for maths teachers"),
        html.Img(src="/assets/icon.png")
    ], className = 'banner'),

        html.Div([        
        dcc.Graph(id='fonction')
    ],
        style={'width': '50%', 'display': 'inline-block'}),


    html.Div([
        dcc.Graph(id='suite')
    ],
    style={'width': '50%', 'display': 'inline-block'}),


        html.Div([
        dcc.Dropdown(id = 'form',
        options=[{'label': 'Parabole en U', 'value': 'U'},
                 {'label': 'Parabole en n', 'value': 'n'}],
        value='U')
        ],
        style={'width': '50%', 'display': 'inline-block'}),

        html.Div([
        dcc.Dropdown(id = 'monotonie',
        options=[{'label': 'Croissante Suite', 'value': 'croi'},
                 {'label': 'Decroissante Suite', 'value': 'decroi'}],
        value='croi')
        ],
        style={'width': '50%', 'display': 'inline-block'})

])

#---------------------------------------------------------------
@app.callback(
    Output(component_id='fonction', component_property='figure'),
    [Input(component_id='form', component_property='value')]
)

def update_output(form):


    fonction = go.Figure()

    if (form == 'U'):
        a = random.randint(0,10)
        b = random.randint(-10,10)
        c = random.randint(-100,100)

        x = np.linspace(-20,20,1000)

        y = a*x**2 + b*x + c
        a_prime = 2*a
        y_prime = a_prime*x + b


        fonction = go.Figure(data=go.Scatter(x=x, y=y))
        fonction.add_trace(go.Scatter(x=x, y=y_prime))
        fonction.update_layout(title = "La fonction : "+str(a)+"x^2 + "+str(b)+"x + "+str(c)+"<br> Sa dérivée : "+str(a_prime)+"x + "+str(b))
        fonction.update_layout(
        title = {
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})

    if (form == 'n'):
        a = random.randint(-10,0)
        b = random.randint(-10,10)
        c = random.randint(-100,100)

        x = np.linspace(-20,20,1000)

        y = a*x**2 + b*x + c
        y_prime = 2*a*x + b

        fonction = go.Figure(data=go.Scatter(x=x, y=y))
        fonction.add_trace(go.Scatter(x=x, y=y_prime))
        fonction.update_layout(title = "La fonction : "+str(a)+"x^2 + "+str(b)+"x + "+str(c)+"<br> Sa dérivée : "+str(a_prime)+"x + "+str(b))
        fonction.update_layout(
        title = {
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})

    return fonction









@app.callback(
    Output(component_id='suite', component_property='figure'),
    [Input(component_id='monotonie', component_property='value')]
)

def update_output(form):
    
    suite = px.bar()

    if (form == 'croi'):
        U1 = random.randint(-10,10)
        r = random.randint(0,10)
        n = random.randint(50,100)
        Un = U1 + (n-1)*r


        X = [(n_loc) for n_loc in range(1,n+1)]
        Y = [U1 + (n_loc-1)*r for n_loc in range(1,n+1)]

        df = pd.DataFrame(X,Y)

        suite = px.bar(df, x=X, y=Y)
        suite.update_layout(title = "La suite : Un = "+str(U1)+" + (n-1) "+str(r)+"<br> C'est une suite croissante")
        suite.update_layout(
        title = {
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})

    if (form == 'decroi'):
        U1 = random.randint(-10,10)
        r = random.randint(-10,0)
        n = random.randint(50,100)
        Un = U1 + (n-1)*r


        X = [(n_loc) for n_loc in range(1,n+1)]
        Y = [U1 + (n_loc-1)*r for n_loc in range(1,n+1)]

        df = pd.DataFrame(X,Y)

        suite = px.bar(df, x=X, y=Y)
        suite.update_layout(title = "La suite : Un = "+str(U1)+" + (n-1) "+str(r)+"<br> C'est une suite décroissante")
        suite.update_layout(
        title = {
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    return suite




if __name__ == '__main__':
    app.run_server(debug=True)