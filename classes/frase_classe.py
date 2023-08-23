from csv_scripts.data_model import DataModel

class Frase_classe:
    def __init__(self, cod_classe, frase, tp_acao):
        self._cod_classe = cod_classe
        self._frase = frase
        self._tp_acao = tp_acao

    @property
    def cod_classe(self):
        return self._cod_classe
    
    @cod_classe.setter
    def cod_classe(self, valor):
        self._cod_classe = valor
    
    @property
    def frase(self):
        return self._frase
    
    @frase.setter
    def frase(self, valor):
        self._frase = valor
    
    @property
    def tp_acao(self):
        return self._tp_acao
    
    @tp_acao.setter
    def tp_acao(self, valor):
        self._tp_acao = valor