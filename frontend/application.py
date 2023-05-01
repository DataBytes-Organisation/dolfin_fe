# Import necessary modules
from app import app, application
from classes.auth import Auth
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from utils.constants import home_page_location, login_location, dashboard_location, breakdown_location, news_location

# Import the various pages of the web app
from pages.home import home
from pages.login import login
from pages.dashboard import dashboard
from pages.breakdown import breakdown
from pages.news import news

# Import callback functions for the sidebar
from layout.sidebar.sidebar_callbacks import toggle_collapse, toggle_classname

# Define a callback function that determines the appropriate page layout based on the current URL pathname
@app.callback(
  Output("page-content", "children"), # Output is the "page-content" div and its children
  Input("url", "pathname"), # Input is the current URL pathname
  State("url", "pathname") # State is the current URL pathname
)
def render_page_content(pathname, state_path):
    # If the current URL pathname is the login page, return the login layout
    if pathname == login_location:
        return login.layout
    # If the user is authenticated...
    if Auth.is_authenticated():
        # Check the current URL pathname and return the appropriate layout for each page
        if pathname == home_page_location:
            return home.layout
        if pathname == dashboard_location:
            return dashboard.layout
        if pathname == breakdown_location:
            return breakdown.layout
        if pathname == news_location:
            return news.layout    
    else:
        # If the user is not authenticated, return a message prompting them to authenticate and redirecting them to the login page
        return dcc.Link("Oh Dear, Appears you need to Authenticate, Click this to head back to login..", href=login_location)

# Run the Flask application
if __name__ == "__main__":
    application.run(port=8080, debug=True, load_dotenv=True)