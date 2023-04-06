from classes.api import API
from dash.dependencies import Input, Output, State
from app import app
import pandas as pd
import plotly.express as px

df = pd.read_csv('pages/breakdown/dummies.csv')

@app.callback(
    Output('yearly_spending_graph', 'figure'),
    Input('yearly_spending_dd', 'value')
)
def update_graph(year):
    dff = df[df.iloc[:,3]==year]
    figln = px.line(dff, x='Month', y='Spending')
    return figln


@app.callback(
    Output('yearly_saving_graph', 'figure'),
    Input('yearly_saving_dd', 'value')
)
def update_graph(year):
    dff = df[df.iloc[:,3]==year]
    figln = px.line(dff, x='Month', y='Saving')
    return figln

# def callback(n):
#     api = API()
#     return f"{n}"