from csv_scripts.data_model import DataModel

class Item:
    def __init__(self, nome, descricao, duracao, efeito, level):
        self.nome = nome
        self.descricao = descricao
        self.duracao = duracao
        self.efeito = efeito
        self.level = level

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, valor):
        self.nome = valor

    @property
    def descricao(self):
        return self.descricao
    
    @descricao.setter
    def descricao(self, valor):
        self.descricao = valor

    @property
    def duracao(self):
        return self.duracao
    
    @duracao.setter
    def duracao(self, valor):
        self.duracao = valor

    @property
    def efeito(self):
        return self.efeito
    
    @efeito.setter
    def efeito(self, valor):
        self.efeito = valor

    @property
    def level(self):
        return self.level
    
    @level.setter
    def level(self, valor):
        self.level = valor   