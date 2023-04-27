from classes.api import API
from dash.dependencies import Input, Output, State
from app import app
import pandas as pd
import plotly.express as px


#Importing calculated savings and spending models. Required data will be summed Amount spent grouped by Year and Month
dfIncoming = pd.read_csv('pages/breakdown/monthly_saving_user.csv')
dfOutgoing = pd.read_csv('pages/breakdown/monthly_spending_user.csv')

#This can probably be done elsewhere as static data. Included to sort values by month and display properly on the graph
ordered_months = ["Jan", "Feb", "Mar", "Apr", "May", "June",
      "July", "Aug", "Sep", "Oct", "Nov", "Dec"]

#Both incoming models are sorted by month
dfIncoming['to_sort']=dfIncoming['month'].apply(lambda x:ordered_months.index(x))
dfIncoming = dfIncoming.sort_values('to_sort')

dfOutgoing['to_sort']=dfOutgoing['month'].apply(lambda x:ordered_months.index(x))
dfOutgoing = dfOutgoing.sort_values('to_sort')

@app.callback(
    Output('yearly_spending_graph', 'figure'),
    Input('yearly_spending_dd', 'value')
)
def update_graph(year):
    dff = dfOutgoing[dfOutgoing.iloc[:,0]==year]
    figln = px.line(dff, x='month', y='amount')
    return figln


@app.callback(
    Output('yearly_saving_graph', 'figure'),
    Input('yearly_saving_dd', 'value')
)
def update_graph(year):
    dff = dfIncoming[dfIncoming.iloc[:,0]==year]
    figln = px.line(dff, x='month', y='amount')
    return figln

# def callback(n):
#     api = API()
#     return f"{n}"