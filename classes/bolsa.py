from csv_scripts.data_model import DataModel

class Bolsa:
    def __init__(self, cod_personagem, cod_item, quantidade):
        self.cod_personagem = cod_personagem
        self.cod_item = cod_item
        self.quantidade = quantidade

    @property
    def cod_personagem(self):
        return self.cod_personagem
    
    @cod_personagem.setter
    def cod_personagem(self, valor):
        self.cod_personagem = valor
    
    @property
    def cod_item(self):
        return self.cod_item
    
    @cod_item.setter
    def cod_item(self, valor):
        self.cod_item = valor
    
    @property
    def quantidade(self):
        return self.quantidade
    
    @quantidade.setter
    def quantidade(self, valor):
        self.quantidade = valor