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
    @app.callback(
    Output(component_id = BAR,component_property = 'children'),
    Input(component_id = DROPDOWN,component_property = 'value')
    )    
    def update_bar_chart(dropdown):
        pub_game = data[["Game","Sales_in_Millions","Publisher"]]
        filtered_data = pd.DataFrame(pub_game.query("Publisher in @dropdown"))
        if filtered_data.shape[0] == 0:
            return dbc.Alert("NO PUBLISHER MAKE SELECTED",color="danger",id=BAR)
        else:
            fig = px.bar(filtered_data, x='Game', y='Sales_in_Millions',
            title = "{} Sales by Publisher".format(dropdown),color = "Game")
        return html.Div(dcc.Graph(figure=fig),id=BAR)
    return html.Div(id=BAR)   
