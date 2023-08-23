from csv_scripts.data_model import DataModel

class Reino:
    def __init__(self, nome):
        self._nome = nome 

    @property 
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor