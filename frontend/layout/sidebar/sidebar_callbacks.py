from dash.dependencies import Input, Output, State
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
    [Output("chat-container-unique", "style"), Output("chat-messages-unique", "children")],
    [Input("chat-button-unique", "n_clicks")],
    [State("chat-container-unique", "style")]
)
def toggle_chatbox(n_clicks, chat_container_style):
    if not chat_container_style:
        chat_container_style = {"display": "none"}

    if n_clicks and n_clicks % 2 != 0:
        chat_container_style["display"] = "block"
    else:
        chat_container_style["display"] = "none"

    # Add any additional logic for handling chat messages

    return chat_container_style, None
