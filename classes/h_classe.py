from csv_scripts.data_model import DataModel

class H_classe:
    def __init__(self, cod_nome, descricao, efeito, dano_fisico, dano_especial, estado, cooldown):
        
        self.cod_nome = cod_nome
        self.descricao = descricao
        self.efeito = efeito
        self.dano_fisico = dano_fisico
        self.dano_especial = dano_especial
        self.estado = estado
        self.cooldown = cooldown

    @property
    def cod_nome(self):
        return self.cod_nome
    
    @cod_nome.setter
    def cod_nome(self, valor):
        self.cod_nome = valor

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
    def dano_fisico(self):
        return self.dano_fisico
    
    @dano_fisico.setter
    def dano_fisico(self, valor):
        self.dano_fisico = valor

    @property 
    def dano_especial(self):
        return self.dano_especial
    
    @dano_especial.setter
    def dano_especial(self, valor):
        self.dano_especial = valor

    @property
    def dano_especial(self):
        return self.dano_especial
    
    @dano_especial.setter
    def dano_especial(self, valor):
        self.dano_especial = valor

    @property
    def estado(self):
        return self.estado
    
    @estado.setter
    def estado(self, valor):
        self.estado = valor

    @property
    def cooldown(self):
        return self.cooldown
    
    @cooldown.setter
    def cooldown(self, valor):
        self.cooldown = valor