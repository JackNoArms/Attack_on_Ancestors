from csv_scripts.data_model import DataModel

class Frase_npc:
    def __init__(self, cod_personagem, frase, tp_acao, funcao, natureza, cod_reino, cod_cidade, cod_localidade):
        self.cod_personagem = cod_personagem
        self.frase = frase
        self.tp_acao = tp_acao
        self.funcao = funcao
        self.natureza = natureza
        self.cod_reino = cod_reino
        self.cod_cidade = cod_cidade
        self.cod_localidade = cod_localidade

    @property
    def cod_personagem(self):
        return self.cod_personagem

    @cod_personagem.setter
    def cod_personagem(self, valor):
        self.cod_personagem = valor 
    
    @property
    def frase(self):
        return self.frase
    
    @frase.setter
    def frase(self, valor):
        self.frase = valor

    @property
    def tp_acao(self):
        return self.tp_acao
    
    @tp_acao.setter
    def tp_acao(self, valor):
        self.tp_acao = valor

    @property
    def funcao(self):
        return self.funcao
    
    @funcao.setter
    def funcao(self, valor):
        self.funcao = valor

    @property
    def natureza(self):
        return self.natureza
    
    @natureza.setter
    def natureza(self, valor):
        self.natureza = valor

    @property
    def cod_reino(self):
        return self.cod_reino
    
    @cod_reino.setter
    def cod_reino(self, valor):
        self.cod_reino = valor

    @property
    def cod_cidade(self):
        return self.cod_cidade
    
    @cod_cidade.setter
    def cod_cidade(self, valor):
        self.cod_cidade = valor

    @property
    def cod_localidade(self):
        return self.cod_localidade
    
    @cod_localidade.setter
    def cod_localidade(self, valor):
        self.cod_localidade = valor