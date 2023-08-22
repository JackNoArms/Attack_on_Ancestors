from csv_scripts.data_model import DataModel

class Acao_personagem:
    def __init__(self, cod_personagem, cod_frase_classe, tp_acao_frase_classe):
        self.cod_personagem = cod_personagem
        self.cod_frase_classe = cod_frase_classe
        self.tp_acao_frase_classe = tp_acao_frase_classe

    @property
    def cod_personagem(self):
        return self.cod_personagem
    
    @cod_personagem.setter
    def cod_personagem(self, valor):
        self.cod_personagem = valor
    
    @property
    def cod_frase_classe(self):
        return self.cod_frase_classe

    @cod_frase_classe.setter
    def cod_frase_classe(self, valor):
        self.cod_frase_classe = valor
    
    @property
    def tp_acao_frase_classe(self):
        return self.tp_acao_frase_classe
    
    @tp_acao_frase_classe.setter
    def tp_acao_frase_classe(self, valor):
        self.tp_acao_frase_classe = valor