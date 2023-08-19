from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.Div("MENU", className="menu-title"),
        html.Ul([
            html.Li("Partida Solo"),
            html.Li("Criar Partida"),
            html.Li("Entrar em Partida"),
            html.Li("Sair")
        ], className="menu-list")
    ], className="menu"),
    html.Audio(id='audio', src='/assets/background_audio.mp3', autoPlay='autoplay', loop='loop'),

       app.css.append_css({
    'external_url': '/assets/styles.css'
})
])

if __name__ == '__main__':
    app.run_server(debug=True)
