from dash import Dash, html, dcc, callback, Input, Output, State
import dash
import os
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1("Leitura de Arquivos CSV"),
        
        dcc.RadioItems(
            id="csv-selector",
            options=[
                {'label': 'Personagens.csv', 'value': 'Personagens.csv'},
                {'label': 'Racas.csv', 'value': 'Racas.csv'},
                {'label': 'Classes.csv', 'value': 'Classes.csv'},
                {'label': 'Estados.csv', 'value': 'Estados.csv'},
                {'label': 'Itens.csv', 'value': 'Itens.csv'},
                {'label': 'Bolsas.csv', 'value': 'Bolsas.csv'},
                {'label': 'Bestiario.csv', 'value': 'Bestiario.csv'},
                {'label': 'Atributos.csv', 'value': 'Atributos.csv'},
                {'label': 'Frases_Narrador.csv', 'value': 'Frases_Narrador.csv'},
                {'label': 'Frases_Classes.csv', 'value': 'Frases_Classes.csv'},
                {'label': 'Acoes_Personagens.csv', 'value': 'Acoes_Personagens.csv'},
                {'label': 'Frases_Npc.csv', 'value': 'Frases_Npc.csv'},
                {'label': 'Reinos.csv', 'value': 'Reinos.csv'},
            ],
            value='Personagens.csv',
            style={'background-color': 'rgba(255, 243, 224, 0.35)'}
        ),
    ], style={'display': 'inline-block', 'width': '40%', 'vertical-align': 'top', 'padding': '20px'}),
    
    html.Div([
        html.H2("Tabela de Dados"),
        html.Div(id="output-table"),
    ], style={'display': 'inline-block', 'width': '55%', 'vertical-align': 'top', 'padding': '20px'}),
    
])

@app.callback(
    Output("output-table", "children"),
    [Input("csv-selector", "value")]
)
def read_csv(selected_csv):
    game_data_path = os.path.join(os.getcwd(), "game_data")
    file_path = os.path.join(game_data_path, selected_csv)
    
    try:
        df = pd.read_csv(file_path)
        table = html.Table(
            [html.Tr([html.Th(col) for col in df.columns])] +
            [html.Tr([html.Td(df.iloc[i][col]) for col in df.columns]) for i in range(len(df))]
        )
    except Exception as e:
        table = html.Pre(f"Erro ao ler o arquivo {selected_csv}: {str(e)}")
    
    return table


if __name__ == '__main__':
    app.run_server(debug=True)