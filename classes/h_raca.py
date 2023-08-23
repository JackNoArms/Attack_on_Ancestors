from csv_scripts.data_model import DataModel

class H_raca:
    def __init__(self, cod_raca, nome, buff, duracao):

        self._cod_raca = cod_raca
        self._nome = nome
        self._buff = buff
        self._duracao = duracao

    @property
    def cod_raca(self):
        return self._cod_raca
    
    @cod_raca.setter
    def cod_raca(self, valor):
        self._cod_raca = valor

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def buff(self):
        return self._buff
    
    @buff.setter
    def buff(self, valor):
        self._buff = valor

    @property
    def duracao(self):
        return self._duracao
    
    @duracao.setter
    def duracao(self, valor):
        self._duracao = valor