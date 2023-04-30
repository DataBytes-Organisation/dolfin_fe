from classes.api import API
from classes.auth import Auth
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import html
from app import app
from classes.forms import Forms
from utils.constants import welcome_location

@app.callback(
    Output("login_form_div", "children"),
    Input("signup_signin_toggle", "value"),
    PreventUpdate=True,
)
def get_login_form(value):
    if value:
        return Forms.sign_up_form()
    return Forms.sign_in_form()

#Sign Up Submit
@app.callback(
    Output("signup_feedback", "children"),
    Input("sign_up_button", "n_clicks"),
    State("sign_up_fname", "value"),
    State("sign_up_lname", "value"),
    State("sign_up_nname", "value"),
    State("sign_up_email", "value"),
    State("sign_up_password", "value"),
    State("sign_up_password_check", "value"),
    PreventUpdate=True,
)
def sign_up_button_click(n,fname,lname,nname,email,password, pass_check):
    try:
            if n > 0:
                if password != pass_check: raise Exception("Please ensure you have typed your password correctly")
                api = API()
                sign_up_result = api.sign_up(fname = fname, lname = lname, nname = nname, email = email, password=password)
                # As this also signs user in, put the results in cache - look up flash cache dict
                return html.H6(f"Welcome, {email}!")
    except Exception as e:
        return f"Error: {e}"
    
#Sign In Submit
@app.callback(
    Output("signin_feedback", "children"),
    Input("sign_in_button", "n_clicks"),
    State("sign_in_email", "value"),
    State("sign_in_password", "value"),
    PreventUpdate=True,
)
def sign_in_button_click(n,email,password):
    try:
        if n > 0:
            api = API()
            sign_in_result = api.sign_in(email = email, password=password)
            tokens = sign_in_result["auth"]
            Auth.set_cache(email, tokens) # put the email and tokens in cache
            return html.H6(f"Welcome, {email}!")
    except Exception as e:
        return f"Error: {e}"




