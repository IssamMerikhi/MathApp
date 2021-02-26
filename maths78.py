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
from random import choice




app = dash.Dash(__name__)
app.title = 'Maths 78'
server = app.server

#---------------------------------------------------------------
app.layout = html.Div([
    html.Div(["Enjoy Maths"], className='titre'),
    html.Div([], style={'width': '30%'} ,className='einstein'),
    html.Div([], className = 'h'),

        html.Div([
        dcc.Dropdown(id = 'type',
        options=[{'label': 'Droites aléatoires', 'value': 'a'},
                 {'label': 'Droites orthogonales', 'value': 'o'},
                 {'label': 'Droites parallèles', 'value': 'p'}],
        value='a')
        ],
        style={'width': '20%',
        'display': 'inline-block',
        'padding-top': '10px',
        'margin-left': '10%',
        'font-family':'-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Open Sans, Helvetica Neue, sans-serif'}),

        html.Div([
        dcc.Dropdown(id = 'monotonie',
        options=[{'label': 'Ari croissante', 'value': 'acroi'},
                 {'label': 'Ari décroissante', 'value': 'adecroi'},
                 {'label': 'Géo croissante', 'value': 'gcroi'},
                 {'label': 'Géo décroissante', 'value': 'gdecroi'}],
        value='acroi')
        ],
        style={'width': '20%',
        'display': 'inline-block',
        'padding-top': '10px',
        'margin-left': '40%',
        'font-family':'-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Open Sans, Helvetica Neue, sans-serif'}),

    html.Div([
        dcc.Graph(id='droites')
    ],
    style={'width': '50%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(id='suite')
    ],
    style={'width': '50%', 'display': 'inline-block'}),


        html.Div([
        dcc.Dropdown(id = 'new',
        options=[{'label': 'Vecteurs aléatoires', 'value': 'A'},
                 {'label': 'Vecteurs orthogonaux', 'value': 'O'}],
        value='A')
        ],
        style={'width': '20%',
        'display': 'inline-block',
        'padding-top': '10px',
        'margin-left': '10%',
        'font-family':'-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Open Sans, Helvetica Neue, sans-serif'}),
 
    html.Div([
    dcc.Dropdown(id = 'form',
       options=[{'label': 'Parabole en U', 'value': 'U'},
                 {'label': 'Parabole en n', 'value': 'n'},
                 {'label': 'Trinome a>0', 'value': 'apos'},
                 {'label': 'Trinome a<0', 'value': 'aneg'}],
        value='U')
        ],
        style={'width': '20%',
        'display': 'inline-block',
        'padding-top': '10px',
        'margin-left': '40%',
        'font-family':'-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Open Sans, Helvetica Neue, sans-serif'}),


    html.Div([
        dcc.Graph(id='produit')
    ],
    style={'width': '50%', 'display': 'inline-block'}),

        html.Div([        
        dcc.Graph(id='fonction')
    ],
        style={'width': '50%', 'display': 'inline-block'}),

    html.Div(["Copyright - Issam Merikhi 2021 - All rights reserved"], className = 'footer'),




])

#---------------------------------------------------------------
@app.callback(
    Output(component_id='fonction', component_property='figure'),
    [Input(component_id='form', component_property='value')]
)

def function_output(form):


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


        fonction = go.Figure(data=go.Scatter(x=x, y=y, name = "f(X)"))
        fonction.add_trace(go.Scatter(x=x, y=y_prime, name = "f'(X)"))
        fonction.update_layout(title = "La fonction : "+str(a)+"x^2 + "+str(b)+"x + "+str(c)+"<br> Sa dérivée : "+str(a_prime)+"x + "+str(b))
        fonction.update_layout(
        title = {
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
        fonction.update_layout(
        xaxis_title="X",
        yaxis_title="Y",
        legend_title="Functions",
        font=dict(
            family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif",
            size=13,
            color="black"
        )
    )

    if (form == 'n'):
        a = random.randint(-10,0)
        b = random.randint(-10,10)
        c = random.randint(-100,100)

        x = np.linspace(-20,20,1000)

        y = a*x**2 + b*x + c
        a_prime = 2*a
        y_prime = a_prime*x + b

        fonction = go.Figure(data=go.Scatter(x=x, y=y, name ="f(X)"))
        fonction.add_trace(go.Scatter(x=x, y=y_prime, name ="f'(X)"))
        fonction.update_layout(title = "La fonction : "+str(a)+"x^2 + "+str(b)+"x + "+str(c)+"<br> Sa dérivée : "+str(a_prime)+"x + "+str(b))
        fonction.update_layout(
        title = {
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'}),
        fonction.update_layout(
        xaxis_title="X",
        yaxis_title="Y",
        legend_title="Functions",
        font=dict(
            family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif",
            size=13,
            color="black"
        )
    )

    if (form == 'apos'):
        a = random.randint(0,10)
        b = random.randint(-10,10)
        c = random.randint(-10,10)

        d = random.randint(-10,10)
        
        x = np.linspace(-100,100,1000)

        y = a*x**3 + b*x**2 + c*x + d
        y_prime = 3*a*x**2 + 2*b*x + c

        a_prime = 3*a
        b_prime = 2*b
        c_prime = c

        fonction = go.Figure(data=go.Scatter(x=x, y=y, name ="f(X)"))
        fonction.add_trace(go.Scatter(x=x, y=y_prime, name ="f'(X)"))
        fonction.update_layout(title = "La fonction : "+str(a)+"x^3 + "+str(b)+"x^2 + "+str(c)+"x +"+str(d)+"<br> Sa dérivée : "+str(a_prime)+"x^2 + "+str(b_prime)+"x +"+str(c_prime))
        fonction.update_layout(
        title = {
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'}),
        fonction.update_layout(
        xaxis_title="X",
        yaxis_title="Y",
        legend_title="Functions",
        font=dict(
            family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif",
            size=13,
            color="black"
        )
    )

    if (form == 'aneg'):
        a = random.randint(-10,0)
        b = random.randint(-10,10)
        c = random.randint(-10,10)

        d = random.randint(-10,10)
        
        x = np.linspace(-100,100,1000)

        y = a*x**3 + b*x**2 + c*x + d
        y_prime = 3*a*x**2 + 2*b*x + c
        a_prime = 3*a
        b_prime = 2*b
        c_prime = c


        fonction = go.Figure(data=go.Scatter(x=x, y=y, name ="f(X)"))
        fonction.add_trace(go.Scatter(x=x, y=y_prime, name ="f'(X)"))
        fonction.update_layout(title = "La fonction : "+str(a_prime)+"x^3 + "+str(b_prime)+"x^2 + "+str(c_prime)+"x +"+str(d)+"<br> Sa dérivée : "+str(3*a_prime)+"x^2 + "+str(2*b)+"x +"+str(c))
        fonction.update_layout(
        title = {
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'}),
        fonction.update_layout(
        xaxis_title="X",
        yaxis_title="Y",
        legend_title="Functions",
        font=dict(
            family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif",
            size=13,
            color="black"
        )
    )

    return fonction









@app.callback(
    Output(component_id='suite', component_property='figure'),
    [Input(component_id='monotonie', component_property='value')]
)

def suite_output(monotonie):
    
    suite = px.bar()

    if (monotonie == 'acroi'):
        U1 = random.randint(-10,10)
        r = random.randint(0,10)
        n = random.randint(50,100)
        Un = U1 + (n-1)*r


        X = [(n_loc) for n_loc in range(1,n+1)]
        Y = [U1 + (n_loc-1)*r for n_loc in range(1,n+1)]

        df = pd.DataFrame(X,Y)

        suite = px.bar(df, x=X, y=Y)
        suite.update_layout(title = "La suite : Un = "+str(U1)+" + (n-1)x"+str(r)+"<br> C'est une suite arithmétique croissante")
        suite.update_layout(
        title = {
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
        suite.update_layout(
        xaxis_title="n",
        yaxis_title="Un",
        font=dict(
            family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif",
            size=13,
            color="black"
        )
    )

    if (monotonie == 'adecroi'):
        U1 = random.randint(-10,10)
        r = random.randint(-10,0)
        n = random.randint(50,100)
        Un = U1 + (n-1)*r


        X = [(n_loc) for n_loc in range(1,n+1)]
        Y = [U1 + (n_loc-1)*r for n_loc in range(1,n+1)]

        df = pd.DataFrame(X,Y)

        suite = px.bar(df, x=X, y=Y)
        suite.update_layout(title = "La suite : Un = "+str(U1)+" + (n-1)"+str(r)+"<br> C'est une suite arithmétique décroissante")
        suite.update_layout(
        title = {
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
        suite.update_layout(
        xaxis_title="n",
        yaxis_title="Un",
        font=dict(
            family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif",
            size=13,
            color="black"
            )
        )


    if (monotonie == 'gcroi'):
        U1 = random.randint(-10,10)
        q = random.randint(2,5)
        n = random.randint(3,6)
        Un = U1 + q**(n-1)


        X = [(n_loc) for n_loc in range(1,n+1)]
        Y = [U1 + q**(n_loc-1) for n_loc in range(1,n+1)]

        df = pd.DataFrame(X,Y)

        suite = px.bar(df, x=X, y=Y)
        suite.update_layout(title = "La suite : Un = "+str(U1)+" + "+str(q)+"^(n-1)<br> C'est une suite géométrique croissante")
        suite.update_layout(
        title = {
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
        suite.update_layout(
        xaxis_title="n",
        yaxis_title="Un",
        font=dict(
            family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif",
            size=13,
            color="black"
            )
        )


    if (monotonie == 'gdecroi'):
        U1 = random.randint(-10,10)
        q = np.random.choice([1/4,1/2,3/4,1])
        n = random.randint(3,6)
        Un = U1 + q**(n-1)


        X = [(n_loc) for n_loc in range(1,n+1)]
        Y = [U1 + q**(n_loc-1) for n_loc in range(1,n+1)]

        df = pd.DataFrame(X,Y)

        suite = px.bar(df, x=X, y=Y)
        suite.update_layout(title = "La suite : Un = "+str(U1)+" + "+str(q)+"^(n-1) <br> C'est une suite géométrique décroissante")
        suite.update_layout(
        title = {
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
        suite.update_layout(
        xaxis_title="n",
        yaxis_title="Un",
        font=dict(
            family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif",
            size=13,
            color="black"
            )
        )

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
                                size = 10                       
                            ),
                            mode='lines+markers',
                            name='AB'))
        produit.add_trace(go.Scatter(x=df2['xCD'], y=df2['yCD'],
                            marker = dict(
                                size = 10                       
                            ),
                            mode='lines+markers',
                            name='CD'))

        produit.update_layout(yaxis=dict(scaleanchor="x", scaleratio=1))
        produit.update_layout(title = "Le vecteur AB : "+str(u)+"<br> Le vecteur CD : "+str(v)+"<br> Le produit scalaire vaut : "+str(((x2-x1)*(x4-x3))+((y2-y1)*(y4-y3))))
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
        produit.update_layout(title = "Le vecteur AB : "+str(u)+"<br> Le vecteur CD : "+str(v)+"<br> Le produit scalaire vaut : "+str((x2-x1)*(x4-x3)+(y2-y1)*(y4-y3)))
        produit.update_layout(
        title = {
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})

    return produit

@app.callback(
    Output(component_id='droites', component_property='figure'),
    [Input(component_id='type', component_property='value')]
)


def droite(type):

    
    droites = go.Figure()

    if (type == 'a'):
        droites = go.Figure()

        a1 = random.randint(1,10)
        b1 = random.randint(-10,10)

        a2 = random.randint(1,10)
        b2 = random.randint(0,10)

        x = np.linspace(-20,20,1000)

        y1 = a1*x + b1
        y2 = a2*x + b2

        droites = go.Figure(data=go.Scatter(x=x, y=y1, name = "y1"))
        droites.add_trace(go.Scatter(x=x, y=y2, name = "y2"))

        droites.update_layout(title = "La droite y1 : "+str(a1)+"x + "+str(b1)+"<br> La droite y2 : "+str(a2)+"x + "+str(b2))
        droites.update_layout(
                title = {
                    'y':0.9,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'})

        
    if (type == 'o'):


        a1 = random.randint(1,10)
        b1 = choice([i for i in range(-11,11) if i != 0])
 

        a2 = -(1/a1)
        b2 = random.randint(0,10)

        x = np.linspace(-20,20,1000)

        y1 = a1*x + b1
        y2 = a2*x + b2

        droites = go.Figure(data=go.Scatter(x=x, y=y1, name = "y1"))
        droites.add_trace(go.Scatter(x=x, y=y2, name = "y2"))

        droites.update_layout(title = "La droite y1 : "+str(a1)+"x + "+str(b1)+"<br> La droite y2 : "+str(a2)+"x + "+str(b2))
        droites.update_layout(
                title = {
                    'y':0.9,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'})
        droites.update_layout(yaxis=dict(scaleanchor="x", scaleratio=1))


        
    if (type == 'p'):

        droites = go.Figure()

        a1 = random.randint(-10,10)
        b1 = random.randint(-10,10)

        a2 = a1
        b2 = random.randint(-10,10)

        x = np.linspace(-20,20,1000)

        y1 = a1*x + b1
        y2 = a2*x + b2

        droites = go.Figure(data=go.Scatter(x=x, y=y1, name = "y1"))
        droites.add_trace(go.Scatter(x=x, y=y2, name = "y2"))

        droites.update_layout(title = "La droite y1 : "+str(a1)+"x + "+str(b1)+"<br> La droite y2 : "+str(a2)+"x + "+str(b2))
        droites.update_layout(
                title = {
                    'y':0.9,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'})

    
    return droites





if __name__ == '__main__':
    app.run_server(debug=True)