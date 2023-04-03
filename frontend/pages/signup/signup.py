import dash_html_components as html
import dash_core_components as dcc
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

bank_institution = html.Div(
    [
        dbc.Label("Bank Institution", html_for="bank_instiution"),
        dcc.Dropdown(
            id="bank_institution",
            options=[
                {"label": "Commonwealth Bank", "value": 1},
                {"label": "ANZ", "value": 2},
                {"label": "NAB", "value": 3},
                {"label": "Westpac", "value": 4},
                {"label": "Bank of Queensland", "value": 5},
                {"label": "Bank of Melbourne", "value": 6},
                {"label": "Bankwest", "value": 7},
                {"label": "Bendigo Bank", "value": 8},
                {"label": "St George Bank", "value": 9},
                {"label": "Suncorp", "value": 10},
            ],
        ),
        html.Br()
    ]
)

bsb = html.Div(
    [
        dbc.Label("Bank BSB", html_for="bsb"),
        dbc.Input(type="tel", id="bsb", placeholder="Enter BSB", pattern="[0-9]{3}-[0-9]{3}"),
        html.Br()
    ],
)

account_no = html.Div(
    [
        dbc.Label("Bank Account Number", html_for="account_no"),
        dbc.Input(type="text", id="account_no", placeholder="Enter Account Number", minlength=6, maxLength=10),
    ],
)

form = dbc.Form([fname, lname, email_input, password_input, bank_institution, bsb, account_no])

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
                    {"key": "1", "src": "/assets/images/plant.jpg"},
                    {"key": "2", "src": "/assets/images/pig.jpg"},
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
            ]
    )
    ]
)
],
)