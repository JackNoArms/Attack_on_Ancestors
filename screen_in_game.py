from dash import Dash, html, dcc, callback, Input, Output, State

app = Dash(__name__)

app.layout = html.Div([
    html.Section(className="layout", children=[
        html.Div("1", className="header"),
        html.Div("2", className="leftSide"),
        html.Div("3", className="body"),
        html.Div("4", className="rightSide"),
        html.Div("5", className="footer"),
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
