import dash_bootstrap_components as dbc
from dash import html
from dash_bootstrap_components._components.Container import Container

navbar = dbc.Navbar(
    # dbc.Container(
    #     [
    #         html.A(
    #             # Use row and col to control vertical alignment of logo / brand

    #                 dbc.Col(html.Img(src="/assets/images/logo_small.png", height="50px")),

    #             #href="https://plotly.com", CHANGE TO DOLFIN HOME ADDRESS
    #             style={"textDecoration": "none"},
    #             id="navbar-logo"
    #         ),
    #     ],
    # ),
    color="#2d7ded",
    dark=True,
    id="navbar",
)
logo = html.Div(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand

                    dbc.Col(html.Img(src="/assets/images/logo_small.png", height="100px")),
                #href="https://plotly.com", CHANGE TO DOLFIN HOME ADDRESS
                style={"textDecoration": "none"},
                id="navbar-logo"
            ),
        ],

)


# add callback for toggling the collapse on small screens
# @app.callback(
#     Output("navbar-collapse", "is_open"),
#     [Input("navbar-toggler", "n_clicks")],
#     [State("navbar-collapse", "is_open")],
# )
# def toggle_navbar_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open