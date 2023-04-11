import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash import dcc, html
from pages.signin import signin_callbacks

email_input = html.Div(
    [
        dbc.Label("Email", html_for="email"),
        dbc.Input(type="email", id="email", placeholder="Enter email"),
        html.Br()
    ],
)

password_input = html.Div(
    [
        dbc.Label("Password", html_for="password"),
        dbc.Input(
            type="password",
            id="password",
            placeholder="Enter password",
        ),
        html.Br()
    ]
)

form = dbc.Form([email_input, password_input])

layout = dbc.Container(
    [
    dbc.Container(
    [
    dbc.Col(
            [
                html.H1("Login To Your Account:", id="submit_header"),
                html.Hr(),
                dbc.Form([form]),
            ],
            id="submit_col1"
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
        ),
        
    ],
    id="submit",
),

dbc.Container(
    [
    dbc.Col(
            [
            html.Button('SIGN IN', id='submit-button', n_clicks=0),
            ]
    )
    ]
)
],
)