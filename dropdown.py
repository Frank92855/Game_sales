from dash import Dash,html,dcc
import dash_bootstrap_components as dbc
import pandas as pd
import os
from util import get_data
from ids import *

PATH = r"C:\Users\Frank\game_sales\Games.csv"

def render(app):
    df = get_data(PATH)
    publishers = df["Publisher"].unique()
    games = [{"label":Name, "value":Name} for Name in publishers]
    return  html.Div(
    [
        dcc.Dropdown(
            options = games,
            value= "Valve",
            placeholder="large dropdown",
            className="mb-3",
            id = DROPDOWN,
            multi=True,
        ),
    ])
