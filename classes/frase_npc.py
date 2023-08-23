from csv_scripts.data_model import DataModel

class Frase_npc:
    def __init__(self, cod_personagem, frase, tp_acao, funcao, natureza, cod_reino, cod_cidade, cod_localidade):
        self._cod_personagem = cod_personagem
        self._frase = frase
        self._tp_acao = tp_acao
        self._funcao = funcao
        self._natureza = natureza
        self._cod_reino = cod_reino
        self._cod_cidade = cod_cidade
        self._cod_localidade = cod_localidade

    @property
    def cod_personagem(self):
        return self._cod_personagem

    @cod_personagem.setter
    def cod_personagem(self, valor):
        self._cod_personagem = valor 
    
    @property
    def frase(self):
        return self._frase
    
    @frase.setter
    def frase(self, valor):
        self._frase = valor

    @property
    def tp_acao(self):
        return self._tp_acao
    
    @tp_acao.setter
    def tp_acao(self, valor):
        self._tp_acao = valor

    @property
    def funcao(self):
        return self._funcao
    
    @funcao.setter
    def funcao(self, valor):
        self._funcao = valor

    @property
    def natureza(self):
        return self._natureza
    
    @natureza.setter
    def natureza(self, valor):
        self._natureza = valor

    @property
    def cod_reino(self):
        return self._cod_reino
    
    @cod_reino.setter
    def cod_reino(self, valor):
        self._cod_reino = valor

    @property
    def cod_cidade(self):
        return self._cod_cidade
    
    @cod_cidade.setter
    def cod_cidade(self, valor):
        self._cod_cidade = valor

    @property
    def cod_localidade(self):
        return self._cod_localidade
    
    @cod_localidade.setter
    def cod_localidade(self, valor):
        self._cod_localidade = valor