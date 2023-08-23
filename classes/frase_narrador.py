from csv_scripts.data_model import DataModel

class Frase_narrador:
    def __init__(self, frase, tp_acao):
        self._frase = frase
        self._tp_acao = tp_acao
    
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