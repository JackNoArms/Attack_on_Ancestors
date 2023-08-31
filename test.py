from dash import Dash, dcc, html, callback, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    # representa a barra de endereço do navegador e não renderiza nada
    dcc.Location(id='url', refresh=False),
    dcc.Link('Navegar para "login"', href='login.py'),
    html.Br(),
    dcc.Link('Navegar para "/page-2"', href='/page-2'),
    # o conteúdo será renderizado neste elemento
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == 'login.py':
        return html.Div([
            html.H3('Página 1')
        ])
    elif pathname == '/page-2':
        return html.Div([
            html.H3('Página 2')
        ])
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
