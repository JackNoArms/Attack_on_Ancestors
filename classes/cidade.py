from csv_scripts.data_model import DataModel

class Cidade:
    def __init__(self, cod_reino, nome):
        self.cod_reino = cod_reino
        self.nome = nome

    @property
    def cod_reino(self):
        return self.cod_reino
    
    @cod_reino.setter
    def cod_reino(self, valor):
        self.cod_reino = valor

    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, valor):
        self.nome = valor