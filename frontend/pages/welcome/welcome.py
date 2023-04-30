import dash_html_components as html
import dash_bootstrap_components as dbc
from classes.auth import Auth

email, _ = Auth.get_cache()

layout = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.H1(f"Welcome, {email}!")
        )
    )
)