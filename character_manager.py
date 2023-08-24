from classes.personagem import Personagem
import pandas as pd
import os

class Character_manager:
    def __init__(self):
        self.jogando = True
    
    def iniciar(self):
        print("Bem vindo ao mundo de Attack on Ancestors")
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


        elif comando == "2":
            self.jogando = False
            print("Saindo do jogo...")

        else:
            print(f"Comando '{comando}' não é válido.")
    
    def character_create(self):
        df = pd.read_csv("game_data/Personagens.csv")
        while True:
            nome = input("Qual o nome do seu personagem?\nComando: ")
            personagem = Personagem(nome=nome)
            comando = input(f"Confirmar o nome '{personagem.nome}'? \n1) Sim \n2) Nao\nComando: ")
            if comando == "1":
                os.system("cls")
                self.nome_personagem = personagem.nome
                novo_registro = pd.DataFrame({'COD': len(df) + 1, 'NOME': personagem.nome, 'GENERO': '', 'RACA': '', 'CLASSE': '', 'LEVEL': 0, 'ESTADO': '', 'VIDA_T': 0, 'VIDA_A': 0, 'MANA_T': 0, 'MANA_A': 0, 'VIGOR_T': 0, 'VIGOR_A': 0, 'DANO_FISICO': 0, 'DANO_ESPECIAL': 0, 'DEFESA': 0, 'DEFESA_ESPECIAL': 0, 'CHANCE_ESQUIVA': 0, 'FORCA': 0, 'DESTREZA': 0, 'CONSTITUICAO': 0, 'CARISMA': 0, 'INTELIGENCIA': 0, 'COD_REINO': 0, 'NPC': 0}, index=[0])
                df_nome = pd.concat([df, novo_registro], ignore_index=True)
                df_nome.to_csv("game_data/Personagens.csv", index=False)
                break
    
    def select_gender(self):
        df = pd.read_csv("game_data/Personagens.csv")
        self.nome_personagem
        if self.nome_personagem in df["NOME"].values:
            while True:
                print("1) Masculino\n2) Feminino")
                genero = input("Qual o seu genero?\nComando: ")
                if genero == "1":
                    os.system("cls")
                    df.loc[df["NOME"] == self.nome_personagem, "GENERO"] = "Masculino"
                    print(f"O Genero selecionado foi 'Masculino'")
                    break
                elif genero == "2":
                    os.system("cls")
                    df.loc[df["NOME"] == self.nome_personagem, "GENERO"] = "Feminino"
                    print(f"O Genero selecionado foi 'Feminino'")
                    break
                else:
                    os.system("cls")
                    print(f"Gênero '{genero}' não encontrado.")

            df.to_csv("game_data/Personagens.csv", index=False)
        else:
            print(f"Personagem '{self.nome_personagem}' não encontrado.")
    
    def select_race(self):
        df = pd.read_csv("game_data/Personagens.csv")
        self.nome_personagem
        if self.nome_personagem in df["NOME"].values:
            df_raca = pd.read_csv("game_data/Racas.csv")
            lista_racas = list(df_raca["NOME"])
            while True:
                os.system("cls")
                print(lista_racas)
                raca = input("Escolha a sua raça?\nComando: ")
                if raca in lista_racas:
                    df.loc[df["NOME"] == self.nome_personagem, "RACA"] = raca
                    df.to_csv("game_data/Personagens.csv", index=False)
                    print(f"A Raça selecionada é '{raca}'")
                    break
                else:
                    print(f"Raça '{raca}' não encontrada na lista de raças disponíveis.")
        else:
            print(f"Personagem '{self.nome_personagem}' não encontrado.")

    def select_class(self):
        df = pd.read_csv("game_data/Personagens.csv")
        self.nome_personagem
        if self.nome_personagem in df["NOME"].values:
            df_classe = pd.read_csv("game_data/Classes.csv")
            lista_classes = list(df_classe["NOME"])
            while True:
                os.system("cls")
                print(lista_classes)
                classe = input("Escolha a sua classe?\nComando: ")
                if classe in lista_classes:
                    df.loc[df["NOME"] == self.nome_personagem, "CLASSE"] = classe
                    df.to_csv("game_data/Personagens.csv", index=False)
                    print(f"A Raça selecionada é '{classe}'")
                    break
                else:
                    print(f"Classe '{classe}' não encontrada na lista de raças disponíveis.")
        else:
            print(f"Personagem '{self.nome_personagem}' não encontrado.")



if __name__ == "__main__":
    jogo = Character_manager()
    jogo.iniciar()
