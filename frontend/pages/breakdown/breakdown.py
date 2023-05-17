import dash  
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.express as px
import pandas as pd
from app import app
from pages.breakdown import breakdown_callbacks

dfIncoming, dfOutgoing = breakdown_callbacks.get_incoming_outgoing_transactions()

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("YOUR FINANCIAL DASHBOARD",
                        className='text-center text-primary mb-4',id="title"),
                width=12)   
    ]),
    
    dbc.Row([
        
        dbc.Col(html.H2("Yearly Spending",
                        className='text-left text-primary mb-4 '), width = 12),
        
        dbc.Col([
            dcc.Dropdown(id = 'yearly_spending_dd', multi = False, placeholder = 'Select a year',
                        options = [{'label':x, 'value':x} for x in sorted(dfOutgoing.iloc[:,0].unique())]),
            
            dcc.Graph(id = 'yearly_spending_graph', figure={})
        ], width = {'size':6}),
        
        dbc.Col(html.P('Shows your spending over the selected year.', className='text-right text-primary, mb-4'),
                width = {'size': 3,'offset' : 1})
        
    ]),
    
    dbc.Row([
        
        dbc.Col(html.H2("Yearly Saving",
                        className='text-left text-primary mb-4 '), width = 12),
        
        dbc.Col([
            dcc.Dropdown(id = 'yearly_saving_dd', multi = False, placeholder = 'Select a year',
                        options = [{'label':x, 'value':x} for x in sorted(dfIncoming.iloc[:,0].unique())]),
            
            dcc.Graph(id = 'yearly_saving_graph', figure={})
        ], width = {'size':6}),
        
        dbc.Col(html.P('Shows your savings over the selected year.', className='text-right text-primary, mb-4'),
                width = {'size': 3, 'offset': 1})
        
    ])
], fluid = False)
