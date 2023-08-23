from csv_scripts.data_model import DataModel

class Localidade:
    def __init__(self, cod_reino, cod_cidade, nome):
        self._cod_reino = cod_reino
        self._cod_cidade = cod_cidade
        self._nome = nome

    @property
    def cod_reino(self):
        return self._cod_reino
    
    @cod_reino.setter
    def cod_reino(self, valor):
        self._cod_reino = valor

    @property
    def cod_cidade(self):
        return self._cod_cidade

    @cod_cidade.setter
    def cod_cidade(self, valor):
        self._cod_cidade = valor
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor