import dash  
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.express as px
import pandas as pd
from app import app
from pages.breakdown import breakdown_callbacks


df = pd.read_csv('pages/breakdown/dummies.csv')

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Breakdown Dashboard",
                        className='text-center text-primary mb-4'),
                width=12)
        
    ]),
    
    dbc.Row([
        
        dbc.Col(html.H2("Yearly Spending",
                        className='text-left text-primary mb-4 '), width = 12),
        
        dbc.Col([
            dcc.Dropdown(id = 'yearly_spending_dd', multi = False, placeholder = 'Select a year',
                        options = [{'label':x, 'value':x} for x in sorted(df.iloc[:,3].unique())]),
            
            dcc.Graph(id = 'yearly_spending_graph', figure={})
        ], width = {'size':6}),
        
        dbc.Col(html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
                       sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\
                       Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris\
                       nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in\
                       reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\
                       Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia\
                       deserunt mollit anim id est laborum.', className='text-right text-primary, mb-4'),
                width = {'size': 3,'offset' : 1})
        
    ]),
    
    
    dbc.Row([
        
        dbc.Col(html.H2("Yearly Saving",
                        className='text-left text-primary mb-4 '), width = 12),
        
        dbc.Col([
            dcc.Dropdown(id = 'yearly_saving_dd', multi = False, placeholder = 'Select a year',
                        options = [{'label':x, 'value':x} for x in sorted(df.iloc[:,3].unique())]),
            
            dcc.Graph(id = 'yearly_saving_graph', figure={})
        ], width = {'size':6}),
        
        dbc.Col(html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
                       sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\
                       Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris\
                       nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in\
                       reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\
                       Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia\
                       deserunt mollit anim id est laborum.', className='text-right text-primary, mb-4'),
                width = {'size': 3, 'offset': 1})
        
    ])
], fluid = False)

