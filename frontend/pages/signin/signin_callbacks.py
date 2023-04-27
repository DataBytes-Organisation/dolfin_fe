from classes.api import API
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from app import app

@app.callback(
    Output("example-output2", "children"),
    Input("submit-button", "n_clicks"),
    State("email", "value"),
    State("password", "value"),
    PreventUpdate=True,
)

def si_on_button_click(n,email,password):
    try:
        if n > 0:
            api = API()
            sign_in_result = api.sign_in(email = email, password=password)
            #print(sign_in_result["username"])
            # TODO - Put the results in cache - look up flash cache dict
            return "Welcome "+sign_in_result["username"]+" you are now logged in."
            #Please fix my horrible string concat

    except Exception as e:
        return f"Error: {e}"


