import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from pages.dashboard import dashboard_callbacks
import pandas as pd
import dash_table
import json

df_outgoing_transactions = dashboard_callbacks.get_outgoing_transactions()
df_absolute_spending_transaction_values = dashboard_callbacks.list_outgoing_transactions()

accounts = dashboard_callbacks.get_accounts()

accounts_df = pd.json_normalize(accounts)

columns = [{"name": i, "id": i} for i in df_absolute_spending_transaction_values.columns]
columns[2]["name"] = "Amount"
columns[6]["name"] = "Category"
columns[7]["name"] = "Year"
columns[8]["name"] = "Month"

layout = dbc.Container([

    dbc.Row([
        html.H1("YOUR SPENDING BREAKDOWN",
                        className='text-center text-primary mb-4', id="title"),  

        html.H3("YEARLY SPENDING CATEGORIES",
                        className='text-center text-primary mb-4'),
        dbc.Row([
        
                dbc.Col(html.P('Chart shows categories of spending over the selected year.', className='text-right text-primary, mb-4'),
                    width = {'size': 3,'offset' : 0}),
                dbc.Col([
                        dcc.Dropdown(id = 'piechart_dd', multi = False, placeholder = 'Select a year',
                        options = [{'label':x, 'value':x} for x in sorted(df_absolute_spending_transaction_values.iloc[:,7].unique())]),
            
                        dcc.Graph(id = 'piechart', figure={})
                ])
            ]
        ),
  
        dbc.Row(
            dash_table.DataTable(
                data = df_outgoing_transactions.to_dict('records'), 
                columns = columns,
                hidden_columns = ["index", "transactionNumber", "id", "status", "direction", "account", "class", "day"],
                style_cell = {'textAlign':'left'},
                    style_header={
                    'backgroundColor': '#4f8fe3',
                    'fontWeight': 'bold'
                    }
                ))
    ])
])