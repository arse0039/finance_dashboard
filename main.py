from dash import Dash
import dash_bootstrap_components as dbc
from src.components.layout import main_layout


def main():
    app = Dash(external_stylesheets=[dbc.themes.QUARTZ])
    app.title = "Financial Dashboard"
    app.layout = main_layout(app)
    app.run()


if __name__ == "__main__":
    main()
