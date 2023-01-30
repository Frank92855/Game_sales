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
    ser_maker = data[["Game","Sales_in_Millions","Publisher","Genre","Developer","Series"]]
    ser_maker = ser_maker.groupby("Series").sum().sort_values("Sales_in_Millions",ascending = False).iloc[:10]
    ser_maker.reset_index(inplace=True)
    fig = px.bar(ser_maker,x='Series', y='Sales_in_Millions',
    title = "Top 10 Sales of Series of games made",color ="Series")
    return html.Div(dcc.Graph(figure=fig),id=BAR3)
    return html.Div(id=BAR3)  