import plotly.express as px
from dash import Dash,html,dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import os
from util import get_data
import dropdown
from ids import *

PATH = r"C:\Users\Frank\game_sales\Games.csv"

def render(app):
    data = get_data(PATH)
    dev_maker = data[["Game","Sales_in_Millions","Publisher","Genre","Developer"]]
    dev_maker = dev_maker.groupby("Developer").count().sort_values("Game",ascending = False).iloc[:10]
    dev_maker.reset_index(inplace=True)
    fig = px.bar(dev_maker,x='Developer', y='Game',
    title = "Top 10 Number of games made by Developer",color = "Developer")
    return html.Div(dcc.Graph(figure=fig),id=BAR2)
    return html.Div(id=BAR2)  