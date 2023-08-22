from typing import Any
from csv_scripts.data_model import DataModel

class Personagem:
    def __init__(self, nome, genero, raca, classe, level, estado, vida_t, vida_a, mana_t, mana_a, vigor_t, vigor_a, dano_fisico, dano_especial, defesa, defesa_especial, chance_esquiva, forca, destreza, constituicao, carisma, inteligencia, cod_reino, cod_cidade, cod_localidade, npc):
                
        self.nome = nome
        self.genero = genero
        self.raca = raca
        self.classe = classe
        self.level = level
        self.estado = estado
        self.vida_t = vida_t
        self.vida_a = vida_a
        self.mana_t = mana_t
        self.mana_a = mana_a
        self.vigor_t = vigor_t
        self.vigor_a = vigor_a
        self.dano_fisico = dano_fisico
        self.dano_especial = dano_especial
        self.defesa = defesa
        self.defesa_especial = defesa_especial
        self.chance_esquiva = chance_esquiva
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.carisma = carisma
        self.inteligencia = inteligencia
        self.cod_reino = cod_reino
        self.codd_cidade = cod_cidade
        self.cod_localidade = cod_localidade
        self.npc = npc
    
    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, valor):
        self.nome = valor

    @property
    def genero(self):
        return self.genero
    
    @genero.setter
    def genero(self, valor):
        self.genero = valor

    @property
    def raca(self):
        return self.raca
    
    @raca.setter
    def raca(self, valor):
        self.raca = valor
    
    @property
    def classe(self):
        return self.classe
    
    @classe.setter
    def classe(self, valor):
        self.classe = valor
    
    @property
    def level(self):
        return self.level
    
    @level.setter
    def level(self, valor):
        self.level = valor
    
    @property
    def estado(self):
        return self.estado
    
    @estado.setter
    def estado(self, valor):
        self.estado = valor
    
    @property
    def vida_t(self):
        return self.vida_t
    
    @vida_t.setter
    def vida_t(self, valor):
        self.vida_t = valor
    
    @property
    def vida_a(self):
        return self.vida_a
    
    @vida_a.setter
    def vida_a(self, valor):
        self.vida_a = valor
    
    @property
    def mana_t(self):
        return self.mana_t

    @mana_t.setter
    def mana_t(self, valor):
        self.mana_t = valor
    
    @property
    def mana_a(self):
        return self.mana_a

    @mana_a.setter
    def mana_a(self, valor):
        self.mana_a
    
    @property
    def vigor_t(self):
        return self.vigor_t
    
    @vigor_t.setter
    def vigor_t(self, valor):
        self.vigor_t = valor
    
    @property
    def vigor_a(self):
        return self.vigor_a
    
    @vigor_a.setter
    def vigor_t(self, valor):
        self.vigor_t = valor
    
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
    def defesa(self):
        return self.defesa

    @defesa.setter
    def defesa(self, valor):
        self.defesa = valor
    
    @property
    def defesa_especial(self):
        return self.defesa_especial
    
    @defesa_especial.setter
    def defesa_especial(self, valor):
        self.defesa_especial = valor

    @property
    def chance_esquiva(self):
        return self.chance_esquiva
    
    @chance_esquiva.setter
    def chance_esquiva(self, valor):
        self.chance_esquiva = valor
    
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
    
    @property
    def npc(self):
        return self.npc
    
    @npc.setter
    def npc(self, valor):
        self.npc = valor