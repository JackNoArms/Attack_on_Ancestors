from csv_scripts.data_model import DataModel

class Atributo:
    def __init__(self, nome, descricao, efeito, proficiencia):
        self._nome = nome
        self._descricao = descricao
        self._efeito = efeito
        self._proficiencia = proficiencia

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
    def proficiencia(self):
        return self._proficiencia
    
    @proficiencia.setter
    def proficiencia(self, valor):
        self._proficiencia = valor