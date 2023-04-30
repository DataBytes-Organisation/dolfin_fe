import dash_bootstrap_components as dbc
from dash import dcc, html
from pages.signup import signup_callbacks

fname = html.Div(
    [
        dbc.Label("First Name", html_for="fname"),
        dbc.Input(type="text", id="fname", placeholder="Enter first name"),
        html.Br()
    ],
)

lname = html.Div(
    [
        dbc.Label("Last Name", html_for="lname"),
        dbc.Input(type="text", id="lname", placeholder="Enter last name"),
        html.Br()
    ],
)

nname = html.Div(
    [
        dbc.Label("Nick Name", html_for="nname"),
        dbc.Input(type="text", id="nname", placeholder="Enter display name"),
        html.Br()
    ],
)

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
password_input = html.Div(
    [
        dbc.Label("Password", html_for="password"),
        dbc.Input(
            type="password",
            id="password",
            placeholder="Re-enter password",
        ),
        html.Br()
    ]
)

form = dbc.Form([fname, lname, nname, email_input, password_input])

layout = dbc.Container(
    [
    dbc.Container(
    [
    dbc.Col(
            [
                html.H1("Create Your Account:", id="submit_header"),
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
            html.Button('JOIN NOW!', id='submit-button', n_clicks=0),
            html.Span(id="example-output", style={"verticalAlign": "middle"}),
            ]
    )
    ]
)
],
)