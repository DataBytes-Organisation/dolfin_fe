import dash_html_components as html
import dash_core_components as dcc

from layout.sidebar.sidebar import sidebar
from layout.navbar.navbar import navbar, logo
from components.footer import Footer  # Import the Footer component

content = html.Div(id="page-content", className="content-container")

# Wrap the content, sidebar, and footer inside a new div with the "page-container" class
page_container = html.Div(
    [
        sidebar,
        content,
        Footer(),  # Add the Footer component
    ],
    className="page-container",
)

layout = html.Div([dcc.Location(id="url"), navbar, logo, page_container])
