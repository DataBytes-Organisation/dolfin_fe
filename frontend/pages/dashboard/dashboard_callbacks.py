from classes.api import API
from dash.dependencies import Input, Output, State
from app import app
from classes.api import API
from dash.dependencies import Input, Output, State
from app import app
import plotly.express as px


# @app.callback(
#     Output("graph", "figure"), 
#     Input("names", "value"), #CHANGE NAMES TO TIMES
#     Input("values", "value"))
# def generate_chart(names, values): #CHANGE NAMES TO TIMES
#     df = px.data.tips() #REPLACE WITH OUR DATA
#     fig = px.pie(df, values=values, names=names, hole=.3) #CHANGE NAMES TO TIMES
#     return fig


# app.run_server(debug=True)