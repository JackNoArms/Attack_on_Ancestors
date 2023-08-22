from csv_scripts.data_model import DataModel

class Equipamentos:
    def __init__(self, nome, buff):
        self.nome = nome
        self.buff = buff

    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, valor):
        self.nome = valor

    @property
    def buff(self):
        return self.buff
    
    @buff.setter
    def buff(self, valor):
        self.buff = valor

    