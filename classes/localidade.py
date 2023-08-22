from csv_scripts.data_model import DataModel

class Localidade:
    def __init__(self, cod_reino, cod_cidade, nome):
        self.cod_reino = cod_reino
        self.cod_cidade = cod_cidade
        self.nome = nome

    @property
    def cod_reino(self):
        return self.cod_reino
    
    @cod_reino.setter
    def cod_reino(self, valor):
        self.cod_reino = valor

    @property
    def cod_cidade(self):
        return self.cod_cidade

    @cod_cidade.setter
    def cod_cidade(self, valor):
        self.cod_cidade = valor
    
    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, valor):
        self.nome = valor