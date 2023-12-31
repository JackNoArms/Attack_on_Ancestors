import csv
import os
from typing import Any
import pandas as pd

class TableModel:
    """
    Classe para manipulação de arquivos CSV.
    """
    def __init__(self, archive_name):
        """
        Inicializa uma nova instância da classe TableModel.

        Args:
            archive_name (str): O nome do arquivo CSV.
        """
        self.archive_name = archive_name + ".csv"
    
    def create_csv(self, columns):
        """
        Cria um novo arquivo CSV com as colunas fornecidas.

        Args:
            columns (list): Uma lista de strings representando as colunas do CSV.
        """
        original_directory = os.getcwd()
        game_data_directory = os.path.join(original_directory, "Attack_on_Ancestors/game_data")

        if not os.path.exists(game_data_directory):
            os.makedirs(game_data_directory)

        os.chdir(game_data_directory)

        archive_name = self.archive_name
        with open(archive_name, mode="w", newline="") as archive_csv:
            writer = csv.DictWriter(archive_csv, fieldnames=columns)
            writer.writeheader()
        print(f"Arquivo {archive_name} criado com sucesso!")

        os.chdir(original_directory)
    
    def exclude_csv(self):
        """
        Exclui o arquivo CSV, se existir.
        """
        archive_name = self.archive_name
        if os.path.exists(archive_name):
            os.remove(archive_name)
    
    def modify_csv(self, archive_name):
        """
        Modifica o nome do arquivo CSV.

        Args:
            archive_name (str): O novo nome do arquivo CSV.
        """
        self.archive_name = archive_name
    
    @property
    def get_archive_name(self):
        """
        Retorna o nome do arquivo CSV.
        """
        return self.archive_name