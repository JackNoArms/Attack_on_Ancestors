from classes.personagem import Personagem
from csv_scripts.data_model import DataModel
from csv_scripts.table_model import TableModel

class AoA_text:
    def __init__(self):
        self.jogando = True
    
    def iniciar(self):
        print("Bem vindo ao mundo de Attack on Ancestors")
        while self.jogando:
            comando = input("Selecione uma opcao: \n1) Novo jogo \n2) Sair\nComando: ")
            self.processar_comando(comando)
    
    def processar_comando(self, comando):

        if comando == "1":
            while True:
                nome = input("Qual o nome do seu personagem?\nComando: ")
                personagem = Personagem(nome=nome)
                comando = input(f"Confirmar o nome '{personagem.nome}'? \n1) Sim \n2) Nao")
                if comando == "1":
                    break
            raca = input("Qual a sua raça?")
        
        elif comando == "2":
            self.jogando = False
            print("Saindo do jogo...")

        else:
            print(f"Comando '{comando}' não é válido.")
    
if __name__ == "__main__":
    jogo = AoA_text()
    jogo.iniciar()