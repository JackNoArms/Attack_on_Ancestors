from dash import Dash, dcc, html, Input, Output, State
import pandas as pd
import os

css_path = os.path.join(os.path.dirname(__file__), "assets", "login.css")

csv_path = os.path.join(os.path.dirname(__file__), "game_data", "Usuarios.csv")
print("CSV Path:", csv_path)
usuarios_df = pd.read_csv(csv_path)

app = Dash(__name__, external_stylesheets=[css_path])

app.layout = html.Div([
    html.Div([
        html.Div("ENTRAR", className='login-title'),
        dcc.Input(placeholder='Usuario', type='text', id='username', className='input-container'),
        dcc.Input(placeholder='Senha', type='password', id='password', className='input-container'),
        html.Div([
            dcc.Checklist(
            options=[{'label': 'Lembrar-me', 'value': 'lembrar-me'}],
            id='lembrar-me-checkbox',
            className='input-container'
        ),
        html.A("Esqueci minha senha", href="#", className='forgot-password')
        ], className='login-options'),
        html.Div(id='output-container-button', children='', className='login-feedback'),
        html.Button('Entrar', id='login-button', n_clicks=0, className='input-container'),
        html.Button('Criar conta', id='create-account-link', n_clicks=0, className='input-container')
], className='login')
])
    
@app.callback(
    Output('output-container-button', 'children'),
    Input('login-button', 'n_clicks'),
    State('username', 'value'),
    State('password', 'value'),
    prevent_initial_call=True
)
    
def login(n_clicks, username, password):
    if n_clicks:
        user_match = usuarios_df[(usuarios_df['USUARIO'] == username) & (usuarios_df['SENHA'] == password)]
        if not user_match.empty:
            return "Login bem-sucedido!"
        else:
            return "Credenciais inválidas!"

if __name__ == '__main__':
    app.run_server(debug=True)
