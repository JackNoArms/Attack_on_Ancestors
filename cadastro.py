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
        html.Div("CADASTRO", className='login-title'),
        dcc.Input(placeholder='Nome de Usuário', type='text', id='new-username', className='input-container'),
        dcc.Input(placeholder='Senha', type='password', id='new-password', className='input-container'),
        dcc.Input(placeholder='E-mail', type='text', id='new-email', className='input-container'),
        html.Button('Cadastrar', id='create-account-button', n_clicks=0, className='input-container'),
        html.Div(id='output-container-create-account', children='', className='login-feedback')
    ], className='login')
])

@app.callback(
    Output('output-container-create-account', 'children'),
    Input('create-account-button', 'n_clicks'),
    State('new-username', 'value'),
    State('new-password', 'value'),
    State('new-email', 'value'),
    prevent_initial_call=True
)
def cadastrar(n_clicks, new_username, new_password, new_email):
    if n_clicks:
        new_data = pd.DataFrame({"COD": [usuarios_df["COD"].max() + 1], "USUARIO": [new_username], "SENHA": [new_password], "EMAIL": [new_email]})
        usuarios_df = pd.concat([usuarios_df, new_data], ignore_index=True)
        usuarios_df.to_csv(csv_path, index=False)
        return "Cadastro realizado com sucesso!"

if __name__ == '__main__':
    app.run_server(debug=True)
