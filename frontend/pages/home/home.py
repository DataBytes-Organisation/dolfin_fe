import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from pages.home import home_callbacks

layout = dbc.Container([
    dbc.Row(
        [
            html.H6("Overview"),
            html.Hr(),
            dbc.Col(
            [
                # dcc.Link(html.Button('Locations'), href=location_page_location),
                # dcc.Link(html.Button('Optimiser'), href=optimiser_page_location),
                # dcc.Link(html.Button('Scheduling'), href=schedule_page_location),
                # dcc.Link(html.Button('Cooke Report'), href=cooke_report_page_location),
            ],
        ),
    ],
    justify="between"
    ),
    html.Hr(),
    dcc.Interval(id='overview-interval-component', interval=120*1000, n_intervals=0),
    html.Button('Submit', id='home-submit-button', n_clicks=0),
    dbc.Row(
        [
            dbc.Col(html.Div(id='overview-div', children=[]), width=12)
        ],
        justify="between",
    ),
    html.Div(id='dummy-display', children = [])
])
