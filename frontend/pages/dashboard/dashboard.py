from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from pages.dashboard import dashboard_callbacks

# TABLE --- ONLY SAMPLE, NEEDS TO BE ALTERED WHEN WE CAN CONNECT TO OUR DATA API
# table = go.Figure(data=[go.Table(
#     header=dict(values=['A Scores', 'B Scores'],
#                 line_color='darkslategray',
#                 fill_color='lightskyblue',
#                 align='left'),
#     cells=dict(values=[[100, 90, 80, 90], # 1st column 
#                        [95, 85, 75, 95]], # 2nd column
#                line_color='darkslategray',
#                fill_color='lightcyan',
#                align='left'))
# ])

layout = dbc.Container([
#PIE CHART

    #---USE THIS ONE ONCE DATA ADDED---
    # [ 
    # html.H4("Your Spending Categories"),
    #     dcc.Graph(id="graph"),
    #     html.P("Time:"),
    #     dcc.Dropdown(
    #         id="times",
    #         options=["Weekly", "Fortnightly", "Monthly", "Yearly", "All Time"],
    #         value="times",
    #         clearable=False,
    #     ),
    # ],


    #SAMPLE PIE CHART---DELETE THIS ONE ONCE DATA ADDED---
    html.H4('Analysis of the restaurant sales'),
        dcc.Graph(id="graph"),
        html.P("Names:"),
        dcc.Dropdown(id='names',
            options=['smoker', 'day', 'time', 'sex'],
            value='day', clearable=False
    ),
    html.P("Values:"),
        dcc.Dropdown(id='values',
            options=['total_bill', 'tip', 'size'],
            value='total_bill', clearable=False
    ),

    ],

    #dashboard_callbacks,
    #table,
)