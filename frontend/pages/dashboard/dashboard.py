import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from pages.dashboard import dashboard_callbacks
import pandas as pd
import dash_table
from datetime import datetime as dt


df = pd.read_csv('pages/dashboard/Transactions_2022Q1.csv')
df.drop(['enrich', 'transactionDate', 'subClass', 'connection','links.self', 'links.account', 'links.institution', 'links.connection', 'subClass.code'],axis = 1, inplace=True)
df['postDate'] = pd.to_datetime(df['postDate'],errors="coerce")
df.set_index('postDate', inplace=True)

layout = dbc.Container([

    dbc.Row([
        html.H1("YOUR SPENDING BREAKDOWN",
            className='text-center text-primary mb-4'),  

        html.H3("SPENDING CATEGORIZATION",
            className='text-center text-primary mb-4')
        ]),

    dbc.Row([

        dbc.Col(
            html.P('Chart shows categories of spending over a period.', className='text-right text-primary, mb-4'),
            width = {'size': 3,'offset' : 0}),

        dbc.Col([
            dcc.DatePickerRange(
                id='transaction_range',
                calendar_orientation='horizontal',
                day_size=35,
                end_date_placeholder_text="End",
                with_portal=False,
                first_day_of_week=0,
                reopen_calendar_on_clear=True,
                is_RTL=False, 
                clearable=True,
                number_of_months_shown=1, 
                min_date_allowed=dt(2022, 1, 1),
                max_date_allowed=dt(2022, 3, 31),
                initial_visible_month=dt(2022, 1, 1),
                start_date=dt(2022, 1, 1).date(),
                end_date=dt(2022, 3, 31).date(),
                display_format='MMM Do, YY',
                month_format='MMMM, YYYY',
                minimum_nights=1,
                persistence=True,
                persisted_props=['start_date'],
                persistence_type='session',

                updatemode='singledate'
                )  
            ],width = {'size': 5,'offset' : 1}),

            dcc.Graph(id = 'piechart', figure={})
            
        ]),

    dbc.Row(
        dash_table.DataTable(
            id = 'transaction_table',
            data = df.to_dict('records'), 
            columns = [{"name": i, "id": i} for i in df.columns],
            style_cell = {'textAlign':'left'},
            style_header={
            'backgroundColor': '#4f8fe3',
            'fontWeight': 'bold'
            },
            page_size=20
            )
        )
])
