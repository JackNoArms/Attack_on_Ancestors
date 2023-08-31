from dash import html

def get_home_layout():
    layout = html.Div([
        html.Div([
            html.Div("MENU", className="menu-title"),
            html.Ul([
                html.Li("Partida Solo"),
                html.Li("Criar Partida"),
                html.Li("Entrar em Partida"),
                html.Li("Sair")
            ], className="menu-list")
        ], className="menu"),
        html.Audio(id='audio', src='/assets/background_audio.mp3', autoPlay='autoplay', loop='loop')
    ])
    return layout
