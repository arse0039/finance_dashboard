from dash import html


def render(app):
    return html.Div(
        children=[
            html.H1(id="main-header", children=app.title),
            html.Hr(),
        ]
    )
