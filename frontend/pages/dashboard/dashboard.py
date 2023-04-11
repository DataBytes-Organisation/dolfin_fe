import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from pages.dashboard import dashboard_callbacks
import pandas as pd
import dash_table


df = pd.read_csv('pages/dashboard/dummies.csv')

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
                        options = [{'label':x, 'value':x} for x in sorted(df.iloc[:,3].unique())]),
            
                        dcc.Graph(id = 'piechart', figure={})
                ])
            ]
        ),
    
        dbc.Row(
            dash_table.DataTable(
                data = df.to_dict('records'), 
                columns = [{"name": i, "id": i} for i in df.columns],
                style_cell = {'textAlign':'left'},
                    style_header={
                    'backgroundColor': '#4f8fe3',
                    'fontWeight': 'bold'
                    }
                ))
    ])
])