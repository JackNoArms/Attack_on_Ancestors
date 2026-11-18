"""Local-only account registration: PBKDF2 hashes stored outside Git."""
from dash import Dash, dcc, html, Input, Output, State

from auth_store import register

app = Dash(__name__, title="Attack on Ancestors — Cadastro")
app.layout = html.Div([
    html.Main([
        html.H1("Attack on Ancestors", className="login-title"),
        html.H2("Criar conta local"),
        dcc.Input(id="new-username", placeholder="Nome de usuário", type="text",
                  className="input-container", maxLength=40),
        dcc.Input(id="new-password", placeholder="Senha com 12 ou mais caracteres",
                  type="password", className="input-container", maxLength=256),
        dcc.Input(id="new-email", placeholder="E-mail", type="email",
                  className="input-container", maxLength=254),
        html.Button("Cadastrar", id="create-account-button", n_clicks=0,
                    className="input-container"),
        html.Div(id="output-container-create-account", className="login-feedback", role="status"),
        html.P("Os dados ficam somente neste computador.", className="login-feedback"),
    ], className="login"),
])


@app.callback(
    Output("output-container-create-account", "children"),
    Input("create-account-button", "n_clicks"),
    State("new-username", "value"),
    State("new-password", "value"),
    State("new-email", "value"),
    prevent_initial_call=True,
)
def cadastrar(n_clicks, new_username, new_password, new_email):
    if not n_clicks:
        return ""
    try:
        return ("Cadastro local criado." if register(new_username, new_password, new_email)
                else "Este nome de usuário já está cadastrado.")
    except ValueError as exc:
        return str(exc)
    except OSError:
        return "Não foi possível salvar o cadastro local."


if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1")
