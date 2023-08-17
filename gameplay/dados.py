import random

class Dados:
    def __init__(self):
        pass

    def play(self, n_dado):
        return random.randint(1, n_dado)