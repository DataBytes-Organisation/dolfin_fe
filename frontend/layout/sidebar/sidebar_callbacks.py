from dash.dependencies import Input, Output, State
from classes.auth import Auth

from app import app


@app.callback(
    Output("sidebar", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar", "className")],
)
def toggle_classname(n, classname):
    if n and classname == "":
        return "collapsed"
    return ""


@app.callback(
    Output("collapse", "is_open"),
    [Input("navbar-toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
     Output(component_id='login-element-to-hide', component_property='style'),
     Output(component_id='logout-element-to-hide', component_property='style'),
     Input(component_id='home-link', component_property='n_clicks'),
     Input(component_id='dash-link', component_property='n_clicks'),
     Input(component_id='brea-link', component_property='n_clicks'),
     Input(component_id='news-link', component_property='n_clicks'),
)
def show_loginlogout(n,m,l,o):
    print("show_loginlogout")
    print(Auth.is_authenticated())
    if Auth.is_authenticated():
        return {"visibility": "hidden","display": "none"},{}
    else:
        return {},{"visibility": "hidden","display": "none"}
    
@app.callback(  
    Output(component_id='dummy1', component_property='value'),
    Input(component_id='logout-element-to-hide', component_property='n_clicks'),
)

def logout(n):
    print("Logging Out")
    print(Auth.is_authenticated())
    Auth.remove_cache()
    print(Auth.is_authenticated())
    return n
