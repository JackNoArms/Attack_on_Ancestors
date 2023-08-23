class Personagem:
    def __init__(self, nome=None, genero=None, raca=None, classe=None, level=None, estado=None, vida_t=None, vida_a=None, mana_t=None, mana_a=None, vigor_t=None, vigor_a=None, dano_fisico=None, dano_especial=None, defesa=None, defesa_especial=None, chance_esquiva=None, forca=None, destreza=None, constituicao=None, carisma=None, inteligencia=None, cod_reino=None, cod_cidade=None, cod_localidade=None, npc=None):
                
        self._nome = nome
        self._genero = genero
        self._raca = raca
        self._classe = classe
        self._level = level
        self._estado = estado
        self._vida_t = vida_t
        self._vida_a = vida_a
        self._mana_t = mana_t
        self._mana_a = mana_a
        self._vigor_t = vigor_t
        self._vigor_a = vigor_a
        self._dano_fisico = dano_fisico
        self._dano_especial = dano_especial
        self._defesa = defesa
        self._defesa_especial = defesa_especial
        self._chance_esquiva = chance_esquiva
        self._forca = forca
        self._destreza = destreza
        self._constituicao = constituicao
        self._carisma = carisma
        self._inteligencia = inteligencia
        self._cod_reino = cod_reino
        self._codd_cidade = cod_cidade
        self._cod_localidade = cod_localidade
        self._npc = npc
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, valor):
        self._genero = valor

    @property
    def raca(self):
        return self._raca
    
    @raca.setter
    def raca(self, valor):
        self._raca = valor
    
    @property
    def classe(self):
        return self._classe
    
    @classe.setter
    def classe(self, valor):
        self._classe = valor
    
    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, valor):
        self._level = valor
    
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, valor):
        self._estado = valor
    
    @property
    def vida_t(self):
        return self._vida_t
    
    @vida_t.setter
    def vida_t(self, valor):
        self._vida_t = valor
    
    @property
    def vida_a(self):
        return self._vida_a
    
    @vida_a.setter
    def vida_a(self, valor):
        self._vida_a = valor
    
    @property
    def mana_t(self):
        return self._mana_t

    @mana_t.setter
    def mana_t(self, valor):
        self._mana_t = valor
    
    @property
    def mana_a(self):
        return self._mana_a

    @mana_a.setter
    def mana_a(self, valor):
        self._mana_a
    
    @property
    def vigor_t(self):
        return self._vigor_t
    
    @vigor_t.setter
    def vigor_t(self, valor):
        self._vigor_t = valor
    
    @property
    def vigor_a(self):
        return self._vigor_a
    
    @vigor_a.setter
    def vigor_t(self, valor):
        self._vigor_t = valor
    
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
    def defesa(self):
        return self._defesa

    @defesa.setter
    def defesa(self, valor):
        self._defesa = valor
    
    @property
    def defesa_especial(self):
        return self._defesa_especial
    
    @defesa_especial.setter
    def defesa_especial(self, valor):
        self._defesa_especial = valor

    @property
    def chance_esquiva(self):
        return self._chance_esquiva
    
    @chance_esquiva.setter
    def chance_esquiva(self, valor):
        self._chance_esquiva = valor
    
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
    
    @property
    def npc(self):
        return self._npc
    
    @npc.setter
    def npc(self, valor):
        self._npc = valor