from dash import Dash, html, dcc, Input, Output
import os
import pandas as pd
import plotly.express as px

app = Dash(__name__)

app.layout = html.Div([
    html.Link(
        rel='stylesheet',
        href='/assets/data_screen.css'  # Caminho para o arquivo CSS na pasta 'assets'
    ),
    
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
        ),
    ]),
    
    html.Div([
        html.H2("Tabela de Dados"),
        html.Div(id="output-table"),
    ]),
    
    html.Div([
        html.H2("Gráfico de Barras de Vida"),
        dcc.Graph(id="health-bar-chart"),
    ]),
])

@app.callback(
    [Output("output-table", "children"),
     Output("health-bar-chart", "figure")],
    [Input("csv-selector", "value")]
)
def read_csv_and_plot(selected_csv):
    game_data_path = os.path.join(os.getcwd(), "game_data")
    file_path = os.path.join(game_data_path, selected_csv)
    
    try:
        df = pd.read_csv(file_path)
        table = html.Table(
            [html.Tr([html.Th(col) for col in df.columns])] +
            [html.Tr([html.Td(df.iloc[i][col]) for col in df.columns]) for i in range(len(df))]
        )

        # Filtrar as colunas desejadas para o gráfico de barras
        columns_to_plot = ['VIDA_T', 'VIDA_A', 'MANA_T', 'MANA_A', 'VIGOR_T', 'VIGOR_A']
        df_filtered = df[columns_to_plot]

        # Criar o gráfico de barras
        fig = px.bar(df_filtered, orientation='h')
        fig.update_layout(title_text='Barras de Vida dos Personagens')

    except Exception as e:
        table = html.Pre(f"Erro ao ler o arquivo {selected_csv}: {str(e)}")
        fig = {}

    return table, fig

if __name__ == '__main__':
    app.run_server(debug=True)
