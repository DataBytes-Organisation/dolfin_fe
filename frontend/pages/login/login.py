import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash import dcc, html
import dash_daq as daq
from pages.login import login_callbacks


layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(id="login_form_div", children=[]),
                        dbc.Row(
                            [
                                dbc.Col(html.H4("Sign in")),
                                dbc.Col(daq.ToggleSwitch(id='signup_signin_toggle', value=False)),
                                dbc.Col(html.H4("Sign Up")),
                            ]
                        ),
                    ],
                    id="submit_col1",
                    width=6,
                ),
                dbc.Col(
                    [
                        dbc.Carousel(
                        items=[
                            {"key": "1", "src": "/assets/images/welcome.png"},
                            {"key": "2", "src": "/assets/images/welcome2.png"},
                        ],
                        controls=True,
                        indicators=True,
                        interval=2000,
                        ride="carousel",
                        id="carousel",
                        ),
                    ],
                    id="submit_col2",
                    width=6,
                ),
            ],
        ),
    ],
)