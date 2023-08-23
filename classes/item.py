from csv_scripts.data_model import DataModel

class Item:
    def __init__(self, nome, descricao, duracao, efeito, level):
        self._nome = nome
        self._descricao = descricao
        self._duracao = duracao
        self._efeito = efeito
        self._level = level

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, valor):
        self._descricao = valor

    @property
    def duracao(self):
        return self._duracao
    
    @duracao.setter
    def duracao(self, valor):
        self._duracao = valor

    @property
    def efeito(self):
        return self._efeito
    
    @efeito.setter
    def efeito(self, valor):
        self._efeito = valor

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, valor):
        self._level = valor   