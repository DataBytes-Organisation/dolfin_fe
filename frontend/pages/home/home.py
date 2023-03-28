import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from pages.home import home_callbacks

layout = dbc.Container(
    [
    dbc.Col(
            [
                html.H2("Add borders", className="display-3"),
                html.Hr(className="my-2"),
                html.P(
                    "Or, keep it light and add a border for some added definition "
                    "to the boundaries of your content."
                ),
            ],
        ),
        dbc.Col(
            [
                dbc.Carousel(
                items=[
                    {"key": "1", "src": "/assets/images/plant.jpg"},
                    {"key": "2", "src": "/assets/images/pig.jpg"},
                ],
                controls=False,
                indicators=False,
                interval=2000,
                ride="carousel",
                ),
            ]
        ),
        
    ]
)
