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
    game_genre = data[["Game","Sales_in_Millions","Publisher","Genre"]]
    game_genre = game_genre.groupby("Genre").sum().sort_values("Sales_in_Millions",ascending = False).iloc[:10]
    game_genre.reset_index(inplace=True)
    fig = px.pie(game_genre,names='Genre', values='Sales_in_Millions',
    title = "Sales by Genre")
    return html.Div(dcc.Graph(figure=fig),id=PIE)
    return html.Div(id=PIE)   