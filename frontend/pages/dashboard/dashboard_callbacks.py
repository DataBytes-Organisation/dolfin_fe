from classes.api import API
from dash.dependencies import Input, Output, State
from app import app
import pandas as pd
import plotly
import plotly.express as px

df = pd.read_csv('pages/dashboard/dummies.csv')


@app.callback(
    Output('piechart', 'figure'),
     Input('piechart_dd', 'value')
)
def update_graph(year):
    dff = df[df.iloc[:,3]==year]
    fig_pie = px.pie(
        data_frame = dff,
        names = "Categories",
        values = 'Amount',
        hole = .3,
        labels = 'Categories'
    )
    return fig_pie