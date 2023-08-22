from csv_scripts.data_model import DataModel

class Atributo:
    def __init__(self, nome, descricao, efeito, proficiencia):
        self.nome = nome
        self.descricao = descricao
        self.efeito = efeito
        self.proficiencia = proficiencia

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
    def proficiencia(self):
        return self.proficiencia
    
    @proficiencia.setter
    def proficiencia(self, valor):
        self.proficiencia = valor