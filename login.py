"""Local-only credential verification screen for prototype accounts.

Verifies a PBKDF2 hash; it does not create an authenticated web session.
"""
from dash import Dash, dcc, html, Input, Output, State

from auth_store import verify

app = Dash(__name__, title="Attack on Ancestors — Entrar")

app.layout = html.Div([
    html.Main([
        html.H1("Attack on Ancestors", className="login-title"),
        html.H2("Entrar na conta local"),
        dcc.Input(id="username", placeholder="Nome de usuário",
                  type="text", className="input-container", maxLength=40),
        dcc.Input(id="password", placeholder="Senha", type="password",
                  className="input-container", maxLength=256),
        html.Button("Verificar credenciais", id="login-button", n_clicks=0,
                    className="input-container"),
        html.Div(id="output-container-button", className="login-feedback",
                 role="status"),
        html.P("A verificação é local e não inicia uma sessão autenticada.",
               className="login-feedback"),
    ], className="login"),
])


@app.callback(
    Output("output-container-button", "children"),
    Input("login-button", "n_clicks"),
    State("username", "value"),
    State("password", "value"),
    prevent_initial_call=True,
)
def login(n_clicks, username, password):
    if not n_clicks:
        return ""
    try:
        return "Credenciais conferidas localmente." if verify(username, password) else "Credenciais inválidas."
    except (ValueError, OSError):
        return "O cadastro local não pôde ser consultado."


if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1")
