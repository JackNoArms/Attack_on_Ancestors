from dash import Dash, html, dcc, Input, Output
import os
import pandas as pd

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
                # ... Outras opções ...
                {'label': 'Reinos.csv', 'value': 'Reinos.csv'},
            ],
            value='Personagens.csv',
        ),
    ]),
    
    html.Div([
        html.H2("Tabela de Dados"),
        html.Div(id="output-table"),
    ]),
    
    html.Div(id="health-mana-vigor-bars")  # Div para exibir as barras de vida, mana e vigor
])

@app.callback(
    Output("output-table", "children"),
    Output("health-mana-vigor-bars", "children"),
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
        
        # Criação das barras de vida, mana e vigor
        health_mana_vigor_bars = []
        for index, row in df.iterrows():
            name = row["NOME"]

            health_bar = html.Div(
                className="character-card",  # Use a classe do estilo para o card
                children=[
                    html.P(f"{name}: ", className="bar-label"),
                    f"({row['VIDA_A']} / {row['VIDA_T']})",
                    html.Div(
                        className="health-bar",
                        style={
                            'width': f'{(row["VIDA_T"] - row["VIDA_A"]) / row["VIDA_T"] * 100}%'
                                    if row["VIDA_T"] != 0 else '100%'
                        }
                    )
                ]
            )

            mana_bar = html.Div(
                className="character-card",  # Use a classe do estilo para o card
                children=[
                    f"({row['MANA_A']} / {row['MANA_T']})",
                    html.Div(
                        className="mana-bar",
                        style={
                            'width': f'{row["MANA_A"] / row["MANA_T"] * 100}%' if row["MANA_T"] != 0 else '0%'
                        }
                    )
                ]
            )

            vigor_bar = html.Div(
                className="character-card",  # Use a classe do estilo para o card
                children=[
                    f"({row['VIGOR_A']} / {row['VIGOR_T']})",
                    html.Div(
                        className="vigor-bar",
                        style={
                            'width': f'{row["VIGOR_A"] / row["VIGOR_T"] * 100}%' if row["VIGOR_T"] != 0 else '0%'
                        }
                    )
                ]
            )

            # Adicione cada conjunto de barras ao contêiner health_mana_vigor_bars
            health_mana_vigor_bars.extend([health_bar, mana_bar, vigor_bar])

    except Exception as e:
        table = html.Pre(f"Erro ao ler o arquivo {selected_csv}: {str(e)}")
        health_mana_vigor_bars = []  # Caso haja erro, não exibe as barras de vida, mana e vigor
    
    return table, health_mana_vigor_bars

if __name__ == '__main__':
    app.run_server(debug=True)
