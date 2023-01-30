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
    pub_maker = data[["Game","Sales_in_Millions","Publisher","Genre"]]
    pub_maker = pub_maker.groupby("Publisher").count().sort_values("Game",ascending = False).iloc[:10]
    pub_maker.reset_index(inplace=True)
    fig = px.bar(pub_maker,x='Publisher', y='Game',
    title = "Top 10 Number of games made by publishers",color="Publisher")
    return html.Div(dcc.Graph(figure=fig),id=BAR1)
    return html.Div(id=BAR1)  