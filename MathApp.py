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
from math import *


# print(px.data.gapminder()[:15])

app = dash.Dash(__name__)
server = app.server

#---------------------------------------------------------------
app.layout = html.Div([

    html.Div([
        html.H2("By maths teachers, for maths teachers"),
        html.Img(src="/assets/icon.png")
    ], className = 'banner'),
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
        style={'width': '50%', 'display': 'inline-block'}),
        html.Div([        
        dcc.Graph(id='fonction')
    ],
        style={'width': '50%', 'display': 'inline-block'}),


    html.Div([
        dcc.Graph(id='suite')
    ],
    style={'width': '50%', 'display': 'inline-block'}),


        html.Div([
        dcc.Dropdown(id = 'new',
        options=[{'label': 'Nouveaux aléatoires', 'value': 'A'},
                 {'label': 'Nouveaux orthogonaux', 'value': 'O'}],
        value='A')
        ],
        style={'width': '50%', 'display': 'inline-block'}),

        html.Div([
        dcc.Dropdown(id = 'intensite',
        options=[{'label': 'I = 1', 'value': '1'},
                 {'label': 'I = 10', 'value': '10'},
                 {'label': 'I = 100', 'value': '100'}],
        value='1')
        ],
        style={'width': '50%', 'display': 'inline-block'}),


    html.Div([
        dcc.Graph(id='produit')
    ],
    style={'width': '50%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(id='son')
    ],
    style={'width': '50%', 'display': 'inline-block'}),
])

#---------------------------------------------------------------
@app.callback(
    Output(component_id='fonction', component_property='figure'),
    [Input(component_id='form', component_property='value')]
)

def update_output(form):


    fonction = go.Figure()

    a_prime = 0

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
        suite.update_layout(title = "La suite : Un = "+str(U1)+" + (n-1)x"+str(r)+"<br> C'est une suite croissante")
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
        suite.update_layout(title = "La suite : Un = "+str(U1)+" + (n-1)"+str(r)+"<br> C'est une suite décroissante")
        suite.update_layout(
        title = {
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    return suite









@app.callback(
    Output(component_id='produit', component_property='figure'),
    [Input(component_id='new', component_property='value')]
)




def produit_scalaire(new):

    produit = go.Figure()

    if (new == 'A'):
        x1 = random.randint(-10,10)
        y1 = random.randint(-10,10)

        A=(x1,y1)

        x2 = random.randint(-10,10)
        y2 = random.randint(-10,10)

        B=(x2,y2)

        x3 = random.randint(-10,10)
        y3 = random.randint(-10,10)

        C=(x3,y3)

        x4 = random.randint(-10,10)
        y4 = random.randint(-10,10)

        D=(x4,y4)

        u = (x2-x1,y2-y1)
        v = (x4-x3,y4-y3)

        df2 = {'xAB': [x1, x2],
            'xCD': [x3, x4],
            'yAB': [y1, y2],
            'yCD': [y3, y4],
                }


        df2 = pd.DataFrame(df2, columns=['xAB', 'xCD', 'yAB', 'yCD'])

        produit.add_trace(go.Scatter(x=df2['xAB'], y=df2['yAB'],
                            marker = dict(
                                symbol = "triangle-right" ,
                                size = 10                       
                            ),
                            mode='lines+markers',
                            name='AB'))
        produit.add_trace(go.Scatter(x=df2['xCD'], y=df2['yCD'],
                            marker = dict(
                                symbol = "triangle-right" ,
                                size = 10                       
                            ),
                            mode='lines+markers',
                            name='CD'))

        produit.update_layout(yaxis=dict(scaleanchor="x", scaleratio=1))
        produit.update_layout(title = "Le vecteur AB : (xB-xA, yB-yA) = "+str(u)+"<br> Le vecteur CD : (xD-xC, yD-yC) = "+str(v)+"<br> Le produit scalaire vaut : "+str(((x2-x1)*(x4-x3))+((y2-y1)*(y4-y3))))
        produit.update_layout(
        title = {
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})

    if (new == 'O'):
        x1 = random.randint(-10,10)
        y1 = random.randint(-10,10)

        A=(x1,y1)

        x2 = x1 + random.randint(0,5)
        y2 = y1 + random.randint(0,5)

        B=(x2,y2)

        u = (x2-x1,y2-y1)


        x3 = random.randint(-10,10)
        y3 = random.randint(-10,10)

        x4 = x3 + random.randint(0,5)
        while (y2 - y1 == 0):
        
            x1 = random.randint(-10,10)
            y1 = random.randint(-10,10)

            A=(x1,y1)

            x2 = x1 + random.randint(0,5)
            y2 = y1 + random.randint(0,5)

            B=(x2,y2)

            u = (x2-x1,y2-y1)


            x3 = random.randint(-10,10)
            y3 = random.randint(-10,10)

            x4 = x3 + random.randint(0,5)


        y4 = (-(x2-x1)*(x4-x3))/(y2-y1) + y3

        v = (x4-x3,y4-y3)


        df2 = {'xAB': [x1, x2],
            'xCD': [x3, x4],
            'yAB': [y1, y2],
            'yCD': [y3, y4],
                }


        df2 = pd.DataFrame(df2, columns=['xAB', 'xCD', 'yAB', 'yCD'])

        produit.add_trace(go.Scatter(x=df2['xAB'], y=df2['yAB'],
                            marker = dict(
                                size = 10                       
                            ),
                            mode='markers+lines',
                            name='AB'))
        produit.add_trace(go.Scatter(x=df2['xCD'], y=df2['yCD'],
                            marker = dict(
                                size = 10                       
                            ),
                            mode='markers+lines',
                            name='CD'))
        produit.update_layout(yaxis=dict(scaleanchor="x", scaleratio=1))
        produit.update_layout(title = "Le vecteur AB : (xB-xA, yB-yA) = "+str(u)+"<br> Le vecteur CD : (xD-xC, yD-yC) = "+str(v)+"<br> Le produit scalaire vaut : "+str((x2-x1)*(x4-x3)+(y2-y1)*(y4-y3)))
        produit.update_layout(
        title = {
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})

    return produit

@app.callback(
    Output(component_id='son', component_property='figure'),
    [Input(component_id='intensite', component_property='value')]
)


def produit_scalaire(intensite):

    son = go.Figure()

    if (intensite == '1'):
        x=np.linspace(0,100,1000)
        R2 = 10*np.log((x*1/4*pi*2)/10**(-12))
        R4 = 10*np.log((x*1/4*pi*4)/10**(-12))
        R8 = 10*np.log((x*1/4*pi*8)/10**(-12))
        R16 = 10*np.log((x*1/4*pi*16)/10**(-12))

        son = go.Figure(go.Scatter(x=x, y= R2))
        son.add_trace(go.Scatter(x=x, y= R4))
        son.add_trace(go.Scatter(x=x, y= R8))
        son.add_trace(go.Scatter(x=x, y= R16))
        
    if (intensite == '10'):

        x=np.linspace(0,100,1000)
        R2 = 10*np.log((x*10/4*pi*2)/10**(-12))
        R4 = 10*np.log((x*10/4*pi*4)/10**(-12))
        R8 = 10*np.log((x*10/4*pi*8)/10**(-12))
        R16 = 10*np.log((x*10/4*pi*16)/10**(-12))

        son = go.Figure(go.Scatter(x=x, y= R2))
        son.add_trace(go.Scatter(x=x, y= R4))
        son.add_trace(go.Scatter(x=x, y= R8))
        son.add_trace(go.Scatter(x=x, y= R16))



    if (intensite == '100'):


        x=np.linspace(0,100,1000)
        R2 = 10*np.log((x*100/4*pi*2)/10**(-12))
        R4 = 10*np.log((x*100/4*pi*4)/10**(-12))
        R8 = 10*np.log((x*100/4*pi*8)/10**(-12))
        R16 = 10*np.log((x*100/4*pi*16)/10**(-12))

        son = go.Figure(go.Scatter(x=x, y= R2))
        son.add_trace(go.Scatter(x=x, y= R4))
        son.add_trace(go.Scatter(x=x, y= R8))
        son.add_trace(go.Scatter(x=x, y= R16))
    
    return son





if __name__ == '__main__':
    app.run_server(debug=True)
