import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from pages.dashboard import dashboard_callbacks
import pandas as pd
import dash_table
import json

df = dashboard_callbacks.get_transaction_data()
accounts = dashboard_callbacks.get_accounts()

# df = pd.json_normalize(test)
accounts_df = pd.json_normalize(accounts)



# df = pd.read_csv('pages/dashboard/processed_user_outgoing_transaction_data.csv')
# columns = [{"name": i, "id": i} for i in df.columns]
# columns[2]["name"] = "Amount"
# columns[6]["name"] = "Category"
# columns[7]["name"] = "Year"
# columns[8]["name"] = "Month"

test = dashboard_callbacks.get_transaction_data()


# df = pd.json_normalize(test)

layout = dbc.Container([

    dbc.Row([
        html.H1("YOUR SPENDING BREAKDOWN",
                        className='text-center text-primary mb-4', id="title"),  

        html.H3("YEARLY SPENDING CATEGORIES",
                        className='text-center text-primary mb-4'),
        # html.H1(test3),
        # dbc.Row([
        
        #         dbc.Col(html.P('Chart shows categories of spending over the selected year.', className='text-right text-primary, mb-4'),
        #             width = {'size': 3,'offset' : 0}),
        #         dbc.Col([
        #                 dcc.Dropdown(id = 'piechart_dd', multi = False, placeholder = 'Select a year',
        #                 options = [{'label':x, 'value':x} for x in sorted(df.iloc[:,7].unique())]),
            
        #                 dcc.Graph(id = 'piechart', figure={})
        #         ])
        #     ]
        # ),

    
        # dbc.Row(
        #     dash_table.DataTable(
        #         data = df.to_dict('records'), 
        #         columns = columns,
        #         hidden_columns = ["index", "transactionNumber", "id", "status", "direction", "account", "class", "day"],
        #         style_cell = {'textAlign':'left'},
        #             style_header={
        #             'backgroundColor': '#4f8fe3',
        #             'fontWeight': 'bold'
        #             }
        #         ))
    ])
])