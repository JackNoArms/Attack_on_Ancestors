from csv_scripts.data_model import DataModel

class Frase_classe:
    def __init__(self, cod_classe, frase, tp_acao):
        self.cod_classe = cod_classe
        self.frase = frase
        self.tp_acao = tp_acao

    @property
    def cod_classe(self):
        return self.cod_classe
    
    @cod_classe.setter
    def cod_classe(self, valor):
        self.cod_classe = valor
    
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