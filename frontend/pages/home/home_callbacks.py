from classes.api import API
from dash.dependencies import Input, Output, State
from app import app

@app.callback(
    Output('overview-div', 'children'),
    Input('home-submit-button', 'n_clicks'))
def callback(n):
    api = API()
    return f"{n}"