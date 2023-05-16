from app import app, application
from classes.auth import Auth
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from utils.constants import home_page_location, login_location, dashboard_location, breakdown_location, news_location

from pages.home import home
from pages.login import login
from pages.dashboard import dashboard
from pages.breakdown import breakdown
from pages.news import news

from layout.sidebar.sidebar_callbacks import toggle_collapse, toggle_classname

unauthenticatedStyle={
    "padding": 16,
    "marginTop": 32,
    "textAlign": "center",
    "fontSize": 32,}

@app.callback(
  Output("page-content", "children"), 
  Input("url", "pathname"),
  State("url", "pathname")
)

def render_page_content(pathname, state_path):
    if pathname == login_location:
        return login.layout
    if Auth.is_authenticated():
        if pathname == home_page_location:
            return home.layout
        if pathname == dashboard_location:
            return dashboard.layout
        if pathname == breakdown_location:
            return breakdown.layout
        if pathname == news_location:
            return news.layout    
    else:
        return dcc.Link("This page is only available when you are logged in. Click this to head back to login.", href=login_location, style=unauthenticatedStyle)

if __name__ == "__main__":
    application.run(port=8080, debug=True, load_dotenv=True)
