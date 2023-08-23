from csv_scripts.data_model import DataModel

class Bolsa:
    def __init__(self, cod_personagem, cod_item, quantidade):
        self._cod_personagem = cod_personagem
        self._cod_item = cod_item
        self._quantidade = quantidade

    @property
    def cod_personagem(self):
        return self._cod_personagem
    
    @cod_personagem.setter
    def cod_personagem(self, valor):
        self._cod_personagem = valor
    
    @property
    def cod_item(self):
        return self._cod_item
    
    @cod_item.setter
    def cod_item(self, valor):
        self._cod_item = valor
    
    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, valor):
        self._quantidade = valor