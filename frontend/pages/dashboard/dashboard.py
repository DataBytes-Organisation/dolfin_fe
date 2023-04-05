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
                        className='text-center text-primary mb-4'),  

        html.H3("MONTHLY SPENDING",
                        className='text-center text-primary mb-4'),
 
        dbc.Row([
        
                dbc.Col(html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\
                        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris\
                        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in\
                        reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\
                        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia\
                        deserunt mollit anim id est laborum.', className='text-right text-primary, mb-4'),
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