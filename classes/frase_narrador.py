from csv_scripts.data_model import DataModel

class Frase_narrador:
    def __init__(self, frase, tp_acao):
        self.frase = frase
        self.tp_acao = tp_acao
    
    @property
    def frase(self):
        return self.frase
    
    @frase.setter
    def frase(self, valor):
        self.frase = valor

    @property
    def tp_acao(self):
        return self.tp_acao
    
    @tp_acao.setter
    def tp_acao(self, valor):
        self.tp_acao = valor