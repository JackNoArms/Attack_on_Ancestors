from dash import Dash, dcc, html, Input, Output, State
import pandas as pd
import os

csv_path = os.path.join(os.path.dirname(__file__), "game_data", "Usuarios.csv")
print("CSV Path:", csv_path)
usuarios_df = pd.read_csv(csv_path)

app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(placeholder='Usuario', type='text', id='username'),
    dcc.Input(placeholder='Senha', type='password', id='password'),
    html.Button('Login', id='login-button', n_clicks=0),
    html.Div(id='output-container-button', children='Digite seu usuario e sua senha depois aperte em login')
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
        if username == "admin" and password == "admin":
            return "Login bem-sucedido!"
        else:
            return "Credenciais inválidas!"

if __name__ == '__main__':
    app.run_server(debug=True)
