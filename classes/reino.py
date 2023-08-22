from csv_scripts.data_model import DataModel

class Reino:
    def __init__(self, nome):
        self.nome = nome 

    @property 
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, valor):
        self.nome = valor