import dash_html_components as html
import dash_bootstrap_components as dbc
from pages.home import home_callbacks
#from components.footer import Footer



main_content = dbc.Container(
    [
        dbc.Container(
            [
                dbc.Col(
                    [
                        html.H1("JOIN DOLFIN TODAY AND START SAVING!", id="home_header"),
                        html.Hr(),
                        html.P(
                            "Simply create an account, link your bank details and begin!",
                            id="home_info",
                        ),
                    ],
                    id="home_col1",
                ),
                dbc.Col(
                    [
                        dbc.Carousel(
                            items=[
                                {"key": "1", "src": "/assets/images/plant.jpg"},
                                {"key": "2", "src": "/assets/images/pig.jpg"},
                            ],
                            controls=True,
                            indicators=True,
                            interval=2000,
                            ride="carousel",
                            id="carousel",
                        ),
                    ],
                    id="home_col2",
                ),
            ],
            id="home",
        ),
        dbc.Container(
            [
                dbc.Col([html.Button("JOIN NOW!", id="home-submit-button", n_clicks=0)],)
            ]
        ),
        
        
    ]
)

layout = dbc.Container([main_content])
