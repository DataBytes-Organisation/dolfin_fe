# Import necessary modules
import dash
import dash_bootstrap_components as dbc
from flask_caching import Cache
from utils.external_assets import FONT_AWSOME, CUSTOM_STYLE
from layout.layout import layout

# Set up the Dash app with Flask server
app = dash.Dash(
    __name__, # Name of the application
    suppress_callback_exceptions=True, # Suppress callback exceptions if True
    external_stylesheets=[ # List of external stylesheets
        dbc.themes.BOOTSTRAP, # Use the Bootstrap theme
        FONT_AWSOME, # Use Font Awesome
        CUSTOM_STYLE # Use a custom stylesheet
    ],
    meta_tags=[ # List of meta tags to include in the HTML head
        {"name": "viewport", "content": "width=device-width, initial-scale=1, maximum-scale=1.2, minimum-scale=0.9"}
    ]
)

# Define the Flask server instance and assign it to a variable named 'application'
application = app.server

# Set up a cache instance using Flask-Caching to cache the app's computed data
cache = Cache(app.server, config={
    'CACHE_TYPE': 'FileSystemCache',
    'CACHE_DIR': 'cache-directory'
})

# Set the app's title to 'DolFin'
app.title = 'DolFin'

# Log a message to the app's logger for testing purposes
app.logger.info('testing log')

# Set the app's layout to the 'layout' variable defined in another file
app.layout = layout
