import random
import string
from data_model import DataModel

def load_reinos(data_model):    
    reinos_data = [
    ["1", "Reino de Avaloria"],
    ["2", "Domínio de Eldoria"],
    ["3", "Terras de Arkania"],
    ["4", "Reino das Chamas"],
    ["5", "União das Águas"]
]
    
    data_model.add_data(reinos_data)

def load_personagens(data_model):
    dados_personagens = [
        ["1", "Lucas", "Humano", "Guerreiro", "10", "Normal", "100", "100", "50", "50", "60", "60", "20", "15", "30", "25", "15", "18", "12", "14", "10", "8", "2", "0"],
        ["2", "Victor", "Elfo", "Mago", "8", "Envenenado", "80", "70", "80", "40", "50", "40", "10", "25", "20", "30", "20", "12", "16", "10", "18", "15", "1", "0"],
        ["3", "Mateus", "Anão", "Cavaleiro", "12", "Normal", "120", "90", "30", "10", "70", "50", "25", "10", "45", "35", "10", "16", "14", "14", "8", "10", "3", "0"],
        ["4", "Stanley", "Orc", "Bárbaro", "6", "Normal", "80", "80", "0", "0", "80", "80", "30", "10", "40", "20", "5", "20", "15", "16", "6", "6", "4", "0"],
        ["5", "Elena", "Elfo", "Arqueiro", "9", "Normal", "90", "90", "60", "50", "40", "40", "15", "10", "25", "30", "25", "14", "18", "12", "12", "10", "5","0"],
        ["6", "NPC1", "Humano", "Guerreiro", "15", "Normal", "80", "80", "50", "50", "60", "60", "10", "10", "20", "20", "10", "12", "12", "10", "8", "8", "9", "1"],
        ["7", "NPC2", "Elfo", "Arqueiro", "18", "Normal", "100", "100", "60", "60", "70", "70", "15", "15", "25", "25", "20", "14", "14", "12", "10", "10", "5", "1"]
    ]
    data_model.add_data(dados_personagens)

def load_racas(data_model):
    dados_racas = [
        ["1", "Humano", "Versátil e adaptável.", "Perícia em várias habilidades"],
        ["2", "Elfo", "Elegantes e ágeis.", "Visão no escuro, habilidades mágicas"],
        ["3", "Anão", "Resistentes e engenhosos.", "Resistência a veneno, habilidades de engenharia"],
        ["4", "Orc", "Fortes e brutais.", "Bônus em Força e habilidades de combate"],
        ["5", "Goblin", "Pequenos e astutos.", "Habilidades de furtividade e sabotagem"]
    ]
    data_model.add_data(dados_racas)

def load_classes(data_model):
    dados_classes = [
        ["1", "Guerreiro", "Mestre das armas e da batalha.", "Habilidades de combate corpo a corpo"],
        ["2", "Mago", "Manipulador de magia arcan", "Habilidades mágicas poderosas"],
        ["3", "Cavaleiro", "Protetor implacável.", "Habilidades defensivas e de montaria"],
        ["4", "Bárbaro", "Força bruta e fúria.", "Habilidades de combate frenético"],
        ["5", "Arqueiro", "Mestre do arco e flecha.", "Habilidades de ataque à distância"]
    ]
    data_model.add_data(dados_classes)

def load_estados(data_model):
    dados_estados = [
        ["1", "Normal", "Estado padrão do personagem.", "Nenhum efeito especial"],
        ["2", "Envenenado", "Envenenamento afetando o personagem.", "Perda gradual de vida"],
        ["3", "Atordoado", "Personagem atordoado e incapaz de agir.", "Incapacidade de ações por um turno"],
        ["4", "Enraizado", "Personagem preso no lugar.", "Incapacidade de se mover por um turno"],
        ["5", "Confuso", "Personagem confuso e desorientado.", "Ações imprevisíveis"]
    ]
    data_model.add_data(dados_estados)

def load_itens(data_model):
    dados_itens = [
        ["1", "Poção de Cura", "Uma poção capaz de restaurar vida do alvo", "10", "15", "20", "25"],
        ["2", "Poção de Mana", "Uma poção capaz de restaurar mana do alvo", "10", "15", "20", "25"],
        ["3", "Poção de Vigor", "Uma poção capaz de restaurar vigor do alvo", "10", "15", "20", "25"],
        ["4", "Poção de Força", "Uma poção capaz de aumentar temporariamente a força do alvo", "2", "3", "4", "5"],
        ["5", "Poção de Agilidade", "Uma poção capaz de aumentar temporariamente a Agilidade do alvo", "2", "3", "4", "5"]
    ]
    data_model.add_data(dados_itens)

def load_bolsas(data_model, data_model_personagens, data_model_itens):
    bolsas_data = []

    # Recuperar os COD's dos personagens e itens
    personagens_data = data_model_personagens.show_data().values.tolist()
    itens_data = data_model_itens.show_data().values.tolist()

    for personagem in personagens_data:
        cod_personagem = personagem[0]
        for _ in range(2):  # Adicionar 2 itens aleatórios para cada personagem
            item_escolhido = random.choice(itens_data)
            cod_item = item_escolhido[0]
            quantidade = str(random.randint(1, 5))  # Quantidade aleatória entre 1 e 5
            bolsas_data.append([cod_personagem, cod_item, quantidade])

    data_model.add_data(bolsas_data)

def generate_random_name():
    # Gerar um nome aleatório com 6 a 10 caracteres
    length = random.randint(6, 10)
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def load_bestiario(data_model, data_model_reinos):
    bestiario_data = []

    # Recuperar os IDs dos reinos
    reinos_data = data_model_reinos.show_data().values.tolist()

    for cod in range(1, 6):  # Adicionar dados para 5 monstros fictícios
        nome = generate_random_name()
        raca = "Besta"
        classe = "Monstro"
        level = str(random.randint(1, 10))
        estado = "Normal"
        vida = str(random.randint(50, 150))
        mana = str(random.randint(20, 80))
        vigor = str(random.randint(30, 100))
        dano_fisico = str(random.randint(10, 30))
        dano_especial = str(random.randint(5, 20))
        defesa = str(random.randint(20, 40))
        defesa_especial = str(random.randint(15, 30))
        chance_esquiva = str(random.randint(5, 20))
        forca = str(random.randint(10, 20))
        destreza = str(random.randint(10, 20))
        constituicao = str(random.randint(10, 20))
        carisma = str(random.randint(5, 15))
        inteligencia = str(random.randint(5, 15))
        turno = str(random.randint(1, 24))  # Horário do dia que o monstro SPAWNA
        cod_reino = random.choice(reinos_data)[0]  # Escolha aleatória de um reino

        bestiario_data.append([str(cod), nome, raca, classe, level, estado, vida, mana, vigor,
                               dano_fisico, dano_especial, defesa, defesa_especial, chance_esquiva,
                               forca, destreza, constituicao, carisma, inteligencia, turno, cod_reino])

    data_model.add_data(bestiario_data)

def load_atributos(data_model):
    atributos_data = [
        ["1", "FORCA", "Mede a força física do personagem.", "Aumenta o dano físico causado.", "6"],
        ["2", "DESTREZA", "Mede a agilidade e coordenação motora do personagem.", "Aumenta a chance de acerto e esquiva.", "8"],
        ["3", "CONSTITUICAO", "Mede a resistência física e vitalidade do personagem.", "Aumenta os pontos de vida e resistência.", "7"],
        ["4", "CARISMA", "Mede o poder de persuasão e liderança do personagem.", "Aumenta a eficácia de habilidades sociais.", "5"],
        ["5", "INTELIGENCIA", "Mede a capacidade de raciocínio e conhecimento do personagem.", "Aumenta o dano mágico e a eficácia de habilidades intelectuais.", "4"]
    ]
    data_model.add_data(atributos_data)

def load_frases_narrador(data_model):
    frases_narrador_data = [
        ["1", "No princípio dos tempos, antes mesmo da existência da vida, os ancestrais surgiram com poderes absolutos.", "Narrativa"],
        ["2", "Cada ancestral deu origem a uma raça que serviria e cuidaria de suas criações.", "Narrativa"],
        ["3", "Com o tempo, porém, alguns ancestrais se corromperam, trazendo desordem e caos ao mundo que haviam criado.", "Narrativa"],
        ["4", "As raças fiéis lutaram contra os ancestrais corrompidos para proteger o equilíbrio e a harmonia das criações.", "Narrativa"],
        ["5", "A batalha entre as raças e os ancestrais corrompidos moldou o destino do mundo, deixando cicatrizes e lendas que ecoariam através das eras.", "Narrativa"]
    ]
    data_model.add_data(frases_narrador_data)

def load_frases_classes(data_model):
    frases_classes_data = [
        ["1", "1", "Você ousa me desafiar, verme covarde? Venha então, e eu mostrarei a você o que é ser um verdadeiro guerreiro!", "Ruim"],
        ["2", "1", "Correr? Eu não sou um covarde! Prepare-se para enfrentar minha fúria implacável!", "Ruim"],
        ["3", "1", "Precisa de equipamento? Minhas armas são forjadas no calor da batalha!", "Neutra"],
        ["4", "1", "Você tem algo para vender? Talvez eu me interesse, se o preço for justo.", "Neutra"],
        ["5", "1", "O caminho que escolherei é o da coragem e da honra. Lutarei até o fim!", "Neutra"],
        ["6", "2", "Claro que ajudaria, afinal, meus conhecimentos podem iluminar o caminho.", "Boa"],
        ["7", "2", "Atacar-me? Tolo! Minhas magias são tão poderosas quanto imprevisíveis.", "Ruim"],
        ["8", "2", "Correr não é uma opção quando se enfrenta a magia. Meus feitiços irão te encontrar.", "Ruim"],
        ["9", "2", "Se precisa de itens mágicos, estou disposto a negociar. Eles podem mudar seu destino.", "Neutra"],
        ["10", "2", "Você tem artefatos mágicos para vender? Sou sempre receptivo a novos objetos encantados.", "Neutra"],
        ["11", "3", "Você necessita de proteção? Minha armadura e escudo estão à sua disposição.", "Boa"],
        ["12", "3", "Atacar-me seria um erro que custaria caro. Sinta o peso de minha espada!", "Ruim"],
        ["13", "3", "Fugir? Essa não é uma escolha sábia quando se enfrenta um cavaleiro!", "Ruim"],
        ["14", "3", "Precisa de algo? Eu também tenho alguns itens para vender, se for do seu interesse.", "Neutra"],
        ["15", "3", "Tem algo para vender? Estou disposto a ouvir sua oferta.", "Neutra"],
        ["16", "4", "Quem ousa me atacar? Meu machado esmagará todos os que cruzarem meu caminho!", "Ruim"],
        ["17", "4", "Fugir? Hahaha, acha mesmo que escapará da fúria do meu machado?!", "Ruim"],
        ["18", "4", "Quer comprar algo? Minhas pilhagens têm as melhores ofertas.", "Neutra"],
        ["19", "4", "Tem algo para vender? Se for valioso, talvez eu o compre.", "Neutra"],
        ["20", "4", "Que caminho seguir? O caminho do bárbaro, cheio de desafios e conquistas!", "Neutra"],
        ["21", "5", "Aceitaria me ajudar? Minhas flechas nunca erram seu alvo.", "Boa"],
        ["22", "5", "Atacar-me à distância? Acho que subestima minha habilidade com o arco.", "Ruim"],
        ["23", "5", "Fugir? Não adianta correr, minhas flechas sempre alcançam.", "Ruim"],
        ["24", "5", "Quer comprar algo? Minhas flechas mágicas podem ser úteis para você.", "Neutra"],
        ["25", "5", "Quer vender algo? Se tiver algo de interesse para um arqueiro, podemos negociar.", "Neutra"],
    ]
    data_model.add_data(frases_classes_data)

def load_acoes_personagens(data_model):
    acoes_personagens = [
        ["1", "1", "1", "Boa"],
        ["2", "1", "2", "Ruim"],
        ["3", "1", "3", "Ruim"],
        ["4", "2", "4", "Neutra"],
        ["5", "2", "5", "Neutra"],
        ["6", "3", "6", "Boa"],
        ["7", "3", "7", "Ruim"],
        ["8", "4", "8", "Neutra"],
        ["9", "4", "9", "Neutra"],
        ["10", "5", "10", "Boa"]
    ]
    
    data_model.add_data(acoes_personagens)

    
def load_frases_npc(data_model):
    
    npc_data = [
        ["1", "6", "Olá, aventureiro! Precisa de itens para suas jornadas?", "Neutra", "Vendedor", "Neutra", "1"],
        ["2", "7", "Ei, você! Está pronto para enfrentar desafios?", "Boa", "Mentor", "Boa", "2"],
        ["3", "7", "Vai encarar meu desafio? Hahaha, boa sorte!", "Ruim", "Mentor", "Boa", "3"],
        ["4", "6", "Bem-vindo, aventureiro! O que você procura?", "Neutra", "Vendedor", "Neutra", "1"],
        ["5", "6", "Se você tem itens valiosos, estou disposto a comprá-los.", "Neutra", "Vendedor", "Neutra", "2"]
    ]
    
    data_model.add_data(npc_data)


if __name__ == "__main__":

    # Crie instâncias do DataModel para cada tabela
    data_model_reinos = DataModel("Reinos.csv")
    data_model_personagens = DataModel("Personagens.csv")
    data_model_racas = DataModel("Racas.csv")
    data_model_classes = DataModel("Classes.csv")
    data_model_estados = DataModel("Estados.csv")
    data_model_itens = DataModel("Itens.csv")
    data_model_bolsas = DataModel("Bolsas.csv")
    data_model_bestiario = DataModel("Bestiario.csv")
    data_model_atributos = DataModel("Atributos.csv")
    data_model_frases_narrador = DataModel("Frases_Narrador.csv")
    data_model_frases_classes = DataModel("Frases_Classes.csv")
    data_model_acoes_personagens = DataModel("Acoes_Personagens.csv")
    data_model_frases_npc = DataModel("Frases_Npc.csv")
    
    # Chame as funções de carga de dados para cada tabela
    load_reinos(data_model_reinos)
    load_personagens(data_model_personagens)
    load_racas(data_model_racas)
    load_classes(data_model_classes)
    load_estados(data_model_estados)
    load_itens(data_model_itens)
    load_bolsas(data_model_bolsas, data_model_personagens, data_model_itens)
    load_bestiario(data_model_bestiario, data_model_reinos)
    load_atributos(data_model_atributos)
    load_frases_narrador(data_model_frases_narrador)
    load_frases_classes(data_model_frases_classes)
    load_acoes_personagens(data_model_acoes_personagens)
    load_frases_npc(data_model_frases_npc)
    
    print("Carga de dados concluída.")
