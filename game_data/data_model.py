import pandas as pd
from table_model import TableModel
import csv

class DataModel:
    """
    Classe para manipulação de dados em arquivos CSV utilizando pandas.

    Attributes:
        archive_name (str): O nome do arquivo CSV a ser manipulado.

    Methods:
        add_data(data: list) -> pd.DataFrame:
            Adiciona uma lista de dados como nova linha ao arquivo CSV.
        
        show_data() -> None:
            Lê e imprime os dados do arquivo CSV.
        
        delete_data(n_cod: int) -> pd.DataFrame:
            Remove a linha correspondente ao 'n_cod' do arquivo CSV e reorganiza os códigos.

        modify_data(n_cod: int, column=None, data=None) -> None:
            Modifica os dados em uma linha específica do arquivo CSV.
    """
    def __init__(self, archive_name: csv):
        """
        Inicializa uma nova instância da classe DataModel.

        Args:
            archive_name (str): O nome do arquivo CSV a ser manipulado.
        """
        self.archive_name = archive_name
    
    def add_data(self, data: list) -> pd.DataFrame:
        """
        Adiciona uma lista de dados como nova linha ao arquivo CSV.

        Args:
            data (list): Uma lista contendo os dados a serem adicionados.

        Returns:
            pd.DataFrame: O DataFrame atualizado após a adição dos dados.
        """
        archive_name = self.archive_name
        df = pd.read_csv(archive_name)
        new_df = pd.DataFrame(data, columns=df.columns)
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_csv(archive_name, index=False)
        return df
    
    def show_data(self):
        """
        Lê e imprime os dados do arquivo CSV.
        """
        df = pd.read_csv(self.archive_name)
        return df
    
    def delete_data(self, n_cod: int):
        """
        Remove a linha correspondente ao 'n_cod' do arquivo CSV e reorganiza os códigos.

        Args:
            n_cod (int): O valor de 'COD' da linha a ser removida.

        Returns:
            Retorna um arquivo CSV.
        """
        df = pd.read_csv(self.archive_name)
        df = df[df['COD'] != n_cod]
        df = df.reset_index(drop=True)
        df['COD'] = range(1, len(df) + 1)
        df.to_csv(self.archive_name, index=False)
        return df

    def modify_data(self, n_cod: int, column=None, data=None) -> None:
        """
        Modifica os dados em uma linha específica do arquivo CSV.

        Args:
            n_cod (int): O valor de 'COD' da linha a ser modificada.
            column (str, optional): O nome da coluna a ser modificada. Padrão é None.
            data (Any, optional): Os novos dados a serem inseridos na linha ou célula. Padrão é None.
        """
        df = pd.read_csv(self.archive_name)

        if n_cod is None:
            raise ValueError("O parâmetro 'n_cod' deve conter um valor.")
        
        if data is None:
            raise ValueError("O parâmetro 'data' deve conter um valor.")
  
        if column is not None and column not in df.columns:
            raise ValueError(f"A coluna '{column}' não foi encontrada no DataFrame.")
    
        if n_cod not in df['COD'].values:
            raise ValueError(f"O valor de 'n_cod' ({n_cod}) não foi encontrado na coluna 'COD' do DataFrame.")

        if column is None:
            df.loc[df['COD'] == n_cod] = data
        else:
            df.loc[df['COD'] == n_cod, column] = data
        
        df.to_csv(self.archive_name, index=False)
