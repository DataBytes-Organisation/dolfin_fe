
from app import app, application
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from utils.constants import home_page_location
from utils.constants import signup_location
from utils.constants import signin_location
from utils.constants import dashboard_location
from utils.constants import breakdown_location
from pages.home import home
from pages.signup import signup
from pages.signin import signin
from pages.dashboard import dashboard
from pages.breakdown import breakdown
from layout.sidebar.sidebar_callbacks import toggle_collapse, toggle_classname

@app.callback(
  Output("page-content", "children"), 
  Input("url", "pathname")
)

def render_page_content(pathname):
    if pathname == home_page_location:
        return home.layout
    if pathname == signup_location:
        return signup.layout
    if pathname == signin_location:
        return signin.layout
    if pathname == dashboard_location:
        return dashboard.layout
    if pathname == breakdown_location:
        return breakdown.layout
    
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

if __name__ == "__main__":
    application.run(port=8080, debug=True, load_dotenv=True)
