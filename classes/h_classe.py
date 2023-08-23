from csv_scripts.data_model import DataModel

class H_classe:
    def __init__(self, cod_nome, descricao, efeito, dano_fisico, dano_especial, estado, cooldown):
        
        self._cod_nome = cod_nome
        self._descricao = descricao
        self._efeito = efeito
        self._dano_fisico = dano_fisico
        self._dano_especial = dano_especial
        self._estado = estado
        self._cooldown = cooldown

    @property
    def cod_nome(self):
        return self._cod_nome
    
    @cod_nome.setter
    def cod_nome(self, valor):
        self._cod_nome = valor

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
    def dano_fisico(self):
        return self._dano_fisico
    
    @dano_fisico.setter
    def dano_fisico(self, valor):
        self._dano_fisico = valor

    @property 
    def dano_especial(self):
        return self._dano_especial
    
    @dano_especial.setter
    def dano_especial(self, valor):
        self._dano_especial = valor

    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, valor):
        self._estado = valor

    @property
    def cooldown(self):
        return self._cooldown
    
    @cooldown.setter
    def cooldown(self, valor):
        self._cooldown = valor