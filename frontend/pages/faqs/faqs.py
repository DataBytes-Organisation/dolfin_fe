import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app

def generate_collapse_card(question, answer, id):
    return dbc.Card([
        dbc.CardHeader(
            html.H2(
                dbc.Button(
                    question,
                    color="link",
                    id=f"button-{id}",
                    style={"color": "black"},
                    className="faq-button",
                )
            ),
        ),
        dbc.Collapse(
            dbc.CardBody(answer),
            id=f"collapse-{id}",
        ),
    ],
    className="faq-card",
    )

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            html.H1("Frequently Asked Questions", id="faq_header", style={"textAlign": "center"}),
                        ),
                        html.Hr(),
                        generate_collapse_card("How do we interact with chatbot?", "This is the answer to question 1.", 1),
                        generate_collapse_card("How do I connect to my Bank Account?", "This is the answer to question 2.", 2),
                        # Add as many questions as you need
                    ],
                    id="faq_col",
                ),
            ],
            id="faq",
        ),
    ]
)

for i in range(1, 3):  # replace 3 with the number of questions + 1
    @app.callback(
        Output(f"collapse-{i}", "is_open"),
        Output(f"button-{i}", "style"),
        [Input(f"button-{i}", "n_clicks")],
        [State(f"collapse-{i}", "is_open")],
    )
    def toggle_collapse(n, is_open):
        if n:
            return not is_open, {"color": "white" if not is_open else "black", "background-color": "black" if not is_open else "white"}
        return is_open, {"color": "black", "background-color": "white"}
