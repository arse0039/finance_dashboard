from dash import Dash, html, dcc
from . import header


def main_layout(app):
    return html.Div(
        children=[
            header.render(app),
        ]
    )
