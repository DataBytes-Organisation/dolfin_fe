import dash
import dash_bootstrap_components as dbc
from flask_caching import Cache
from utils.external_assets import FONT_AWSOME, CUSTOM_STYLE
from layout.layout import layout

app = dash.Dash(
    __name__,
    # server=application,
    suppress_callback_exceptions=True, 
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        FONT_AWSOME,
        CUSTOM_STYLE
    ],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1, maximum-scale=1.2, minimum-scale=0.9"}
    ]
)
application = app.server # define flask application.server

cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

app.title = 'DolFin'
app.logger.info('testing log')
app.layout = layout