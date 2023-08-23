from csv_scripts.data_model import DataModel

class Classe:
    def __init__(self, nome, descricao, forca, destreza, constituicao, carisma, inteligencia):
        self._nome = nome
        self._descricao = descricao
        self._forca = forca
        self._destreza = destreza
        self._constituicao = constituicao
        self._carisma = carisma
        self._inteligencia = inteligencia
    
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
    def forca(self):
        return self._forca
    
    @forca.setter
    def forca(self, valor):
        self._forca = valor
    
    @property
    def destreza(self):
        return self._destreza
    
    @destreza.setter
    def destreza(self, valor):
        self._destreza = valor
    
    @property
    def constituicao(self):
        return self._constituicao
    
    @constituicao.setter
    def constituicao(self, valor):
        self._constituicao = valor
    
    @property
    def carisma(self):
        return self._carisma
    
    @carisma.setter
    def carisma(self, valor):
        self._carisma = valor
    
    @property
    def inteligencia(self):
        return self._inteligencia

    @inteligencia.setter
    def inteligencia(self, valor):
        self._inteligencia = valor