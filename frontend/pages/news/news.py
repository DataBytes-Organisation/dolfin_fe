import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
from pages.news.data import news_data

# Define the layout for the news page
layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1('News', className='text-center'),
                        html.Hr(),
                    ],
                    className='mb-3 mt-3'
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H3(news_item['title'], className='card-title'),
                                    html.P(news_item['description'], className='card-text'),
                                    dbc.Button('Read more', color='primary', href=f"/news/{news_item['id']}")
                                ]
                            ),
                            className='mb-3'
                        )
                        for news_item in news_data
                    ]
                )
            ]
        ),
    ],
    fluid=True
)
