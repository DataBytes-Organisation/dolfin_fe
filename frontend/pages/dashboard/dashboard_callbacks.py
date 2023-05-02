import dash
from classes.api import API
from dash.dependencies import Input, Output, State
from app import app
import pandas as pd
import plotly
import plotly.express as px




df = pd.read_csv('pages/dashboard/Transactions_2022Q1.csv')

@app.callback(
    Output("transaction_table", "data"),
    [
        Input("transaction_range", "start_date"),
        Input("transaction_range", "end_date"),
    ],
)
def update_table(start_date, end_date):

    data = df.to_dict("records")
    if start_date and end_date:
        mask = (df['postDate'] >= start_date) & (df['postDate'] <= end_date)
        data = df.loc[mask].to_dict("records")
    return data


@app.callback(
    Output('piechart', 'figure'),
    [
    Input("transaction_range", "start_date"),
    Input("transaction_range", "end_date"),
    ],
)
def update_graph(start_date, end_date):

    if start_date and end_date:
        mask = (df['postDate'] >= start_date) & (df['postDate'] <= end_date)
        data = df.loc[mask]

    data = data[data['direction'] == 'debit']
    data['amount'] = data['amount'].astype('float64')
    data['amount'] = data['amount'].abs()

    fig_pie = px.pie(
        data_frame = data,
        names = "subClass.title",
        values = 'amount',
        hole = .3,
        labels = "subClass.title"
    )
    return fig_pie