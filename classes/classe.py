from csv_scripts.data_model import DataModel

class Classe:
    def __init__(self, nome, descricao, forca, destreza, constituicao, carisma, inteligencia):
        self.nome = nome
        self.descricao = descricao
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.carisma = carisma
        self.inteligencia = inteligencia
    
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
    def forca(self):
        return self.forca
    
    @forca.setter
    def forca(self, valor):
        self.forca = valor
    
    @property
    def destreza(self):
        return self.destreza
    
    @destreza.setter
    def destreza(self, valor):
        self.destreza = valor
    
    @property
    def constituicao(self):
        return self.constituicao
    
    @constituicao.setter
    def constituicao(self, valor):
        self.constituicao = valor
    
    @property
    def carisma(self):
        return self.carisma
    
    @carisma.setter
    def carisma(self, valor):
        self.carisma = valor
    
    @property
    def inteligencia(self):
        return self.inteligencia

    @inteligencia.setter
    def inteligencia(self, valor):
        self.inteligencia = valor