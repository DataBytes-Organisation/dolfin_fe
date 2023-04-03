from dash import html
from dash import dcc

from layout.sidebar.sidebar import sidebar
from layout.navbar.navbar import navbar,logo


content = html.Div(id="page-content")

layout = html.Div([dcc.Location(id="url"),navbar, logo, sidebar, content])