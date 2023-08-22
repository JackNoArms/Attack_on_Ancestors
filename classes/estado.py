from csv_scripts.data_model import DataModel

class Estado:
    def __init__(self, nome, descricao, efeito, duracao):
        self.nome = nome
        self.descricao = descricao
        self.efeito = efeito
        self.duracao = duracao

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
    def efeito(self):
        return self.efeito
    
    @efeito.setter
    def efeito(self, valor):
        self.efeito = valor
    
    @property
    def duracao(self):
        return self.duracao
    
    @duracao.setter
    def duracao(self, valor):
        self.duracao = valor