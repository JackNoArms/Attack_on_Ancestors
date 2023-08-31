from classes.personagem import Personagem
import pandas as pd
import os

class Xp_manager:
    def __init__(self):
        self.jogando = True
    
    def iniciar(self):
        print("Bem vindo ao sistema de XP do mundo de Attack on Ancestors")
        while self.jogando:
            comando = input("Selecione uma opcao: \n1) Novo jogo \n2) Sair\nComando: ")
            self.processar_comando(comando)
    
    def processar_comando(self, comando):
        os.system("cls")
        if comando == "1":
            self.character_create()
            self.select_gender()
            self.select_race()
            self.select_class()
            self.attribute_modifiers()

        elif comando == "2":
            self.jogando = False
            print("Saindo do jogo...")

        else:
            print(f"Comando '{comando}' não é válido.")


if __name__ == "__main__":
    jogo = Character_manager()
    jogo.iniciar()
