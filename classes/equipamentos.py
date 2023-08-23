from csv_scripts.data_model import DataModel

class Equipamentos:
    def __init__(self, nome, buff):
        self._nome = nome
        self._buff = buff

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def buff(self):
        return self._buff
    
    @buff.setter
    def buff(self, valor):
        self._buff = valor

    