from csv_scripts.data_model import DataModel

class Estado:
    def __init__(self, nome, descricao, efeito, duracao):
        self._nome = nome
        self._descricao = descricao
        self._efeito = efeito
        self._duracao = duracao

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
    def efeito(self):
        return self._efeito
    
    @efeito.setter
    def efeito(self, valor):
        self._efeito = valor
    
    @property
    def duracao(self):
        return self._duracao
    
    @duracao.setter
    def duracao(self, valor):
        self._duracao = valor