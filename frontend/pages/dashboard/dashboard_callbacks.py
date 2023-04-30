from classes.api import API
from dash.dependencies import Input, Output, State
from app import app
import pandas as pd
import plotly
import plotly.express as px

#The data for the dashboard will need to be positive values
df = pd.read_csv('pages/dashboard/processed_user_outgoing_transaction_data.csv')


@app.callback(
    Output('piechart', 'figure'),
     Input('piechart_dd', 'value')
)
def update_graph(year):
    dff = df[df.iloc[:,8]==year]
    fig_pie = px.pie(
        data_frame = dff,
        names = "category",
        values = 'amount',
        hole = .3,
        labels = 'category'
    )
    return fig_pie

# def get_transaction_data():
#     api = API()
#     transaction_result = api.dashboard()
#     return transaction_result
