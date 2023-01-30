from dash import Dash, html
import dash_bootstrap_components as dbc
# from dash_bootstrap_templates import ThemeChangerAIO
# import bar_chart
import dropdown
import bar_chart
import pie_chart
import bar_chart1
import bar_chart2
import bar_chart3

def create_layout(app):
    return dbc.Container(children=[
        html.H1(
                "Game Sales Analytics", className="header-title"
                ),
        html.P(
                "Based on Steam sale data we can analyze which publisher sells the most games.",
                className="header-description",
                ),
        dropdown.render(app),
        bar_chart.render(app),
        dbc.Row([
        dbc.Col([bar_chart1.render(app)], lg = 6),
        dbc.Col([bar_chart2.render(app)], lg = 6)
        ]),
        dbc.Row([
        dbc.Col([pie_chart.render(app)], lg = 6),
        dbc.Col([bar_chart3.render(app)], lg = 6)
        ])
    ])