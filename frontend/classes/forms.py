import dash_bootstrap_components as dbc
from dash import dcc, html

class Forms:
    def __init__(self) -> None:
        pass

    def sign_in_form():
        return dbc.Form(
            [
                dbc.Row(
                    [
                        html.H1("Login To Your Account", id="submit_header"),
                        html.Div(id="signin_feedback"),
                        
                        dbc.Label("Email", html_for="email"),
                        dbc.Input(type="email", id="sign_in_email", placeholder="Enter email"),

                        dbc.Label("Password", html_for="password"),
                        dbc.Input(type="password", id="sign_in_password", placeholder="Enter password"),
                    ]
                ),
                dbc.Row(
                    dbc.Col(
                        html.Div(dbc.Button('SIGN IN', id='sign_in_button', n_clicks=0), style={'padding': 20}),
                    ),
                    justify="evenly",
                ),
            ],
        )
    
    def sign_up_form():
        return dbc.Form(
            [
                dbc.Row(
                    [
                        html.H1("Create Your Account", id="submit_header"),
                        html.Div(id="signup_feedback"),
                        
                        dbc.Label("First Name", html_for="fname"),
                        dbc.Input(type="text", id="sign_up_fname", placeholder="Enter first name"),

                        dbc.Label("Last Name", html_for="lname"),
                        dbc.Input(type="text", id="sign_up_lname", placeholder="Enter last name"),

                        dbc.Label("Nick Name", html_for="nname"),
                        dbc.Input(type="text", id="sign_up_nname", placeholder="Enter display name"),

                        dbc.Label("Email", html_for="email"),
                        dbc.Input(type="email", id="sign_up_email", placeholder="Enter email"),


                        dbc.Label("Password", html_for="password"),
                        dbc.Input(type="password", id="sign_up_password", placeholder="Enter password"),

                        dbc.Label("Password, Again", html_for="password"),
                        dbc.Input(type="password", id="sign_up_password_check", placeholder="Re-Enter password"),
                    ]
                ),
                dbc.Row(
                    dbc.Col(
                        html.Div(dbc.Button('SIGN UP', id='sign_up_button', n_clicks=0), style={'padding': 20}),
                    ),
                    justify="evenly",
                ),
            ],
        )
