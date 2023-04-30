from classes.api import API
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from app import app

@app.callback(
    Output("example-output", "children"),
    Input("submit-button", "n_clicks"),
    State("fname", "value"),
    State("lname", "value"),
    State("nname", "value"),
    State("email", "value"),
    State("password", "value"),
    PreventUpdate=True,
)

def su_on_button_click(n,fname,lname,nname,email,password):
    try:
            if n > 0:
                api = API()
                sign_up_result = api.sign_up(fname = fname, lname = lname, nname = nname, email = email, password=password)
                # As this also signs user in, put the results in cache - look up flash cache dict
                return "Welcome "+sign_up_result["username"]+" you are now signed up and logged in."

    except Exception as e:
        return f"Error: {e}"