import random
import string
import os
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
        ["1", "Personagem1", "Masculino", "Humano", "Guerreiro", "1", "Normal", "100", "100", "50", "50", "75", "75", "20", "30", "15", "20", "10", "25", "20", "15", "18", "22", "10", "5", "1", "1", "1", "0"],
        ["2", "Personagem2", "Feminino", "Elfo", "Mago", "1", "Normal", "80", "80", "100", "100", "60", "60", "10", "50", "5", "10", "20", "10", "5", "5", "10", "25", "5", "0", "1", "1", "1", "0"],
        ["3", "Personagem3", "Masculino", "Anão", "Guerreiro", "1", "Normal", "120", "120", "30", "30", "80", "80", "25", "15", "25", "15", "5", "30", "20", "25", "12", "18", "10", "3", "1", "1", "1", "0"],
        ["4", "Personagem4", "Feminino", "Orc", "Ladino", "1", "Normal", "150", "150", "20", "20", "90", "90", "15", "40", "10", "15", "15", "20", "30", "10", "8", "10", "20", "1", "1", "1", "0"],
        ["5", "Personagem5", "Masculino", "Goblin", "Arqueiro", "1", "Normal", "90", "90", "60", "60", "40", "40", "25", "30", "10", "20", "5", "15", "30", "15", "15", "20", "30", "1", "1", "1", "0"]
]
    data_model.add_data(dados_personagens)

def load_racas(data_model):
    dados_racas = [
        ["1", "Humano", "Versátil e adaptável.", "5", "5", "5", "5", "5"],
        ["2", "Elfo", "Elegantes e ágeis.", "2", "7", "4", "7", "5"],
        ["3", "Anão", "Resistentes e engenhosos.", "7", "3", "7", "2", "6"],
        ["4", "Orc", "Fortes e brutais.", "9", "4", "9", "1", "2"],
        ["5", "Galoman", "Rápidos e ferozes.", "1", "10", "3", "7", "4"],
        ["6", "Calangoman", "Répteis ágeis.", "1", "10", "5", "4", "5"],   
        ["7", "Loboman", "Violentos e implacáveis.", "7", "8", "7", "0", "3"],        
        ["8", "Tubarãoman", "Vorazes e agressivos.", "8", "7", "8", "0", "2"],    
        ["9", "Stoneman", "Justos e pacíficos.", "1", "10", "0", "4", "10"]    
    ]
    data_model.add_data(dados_racas)

def load_classes(data_model):
    dados_classes = [
        ["1", "Guerreiro", "Mestre das armas e da batalha.", "1", "1", "2", "1", "1"],
        ["2", "Especialista", "Detentor de habilidades especiais.", "0", "0", "1", "2", "3"],
        ["3", "Bardo", "Usuário da arte musical.", "0", "0", "1", "3", "2"],
        ["4", "Domador", "Pega emprestado o poder das feras.", "1", "2", "3", "0", "0"],
        ["5", "Caçador", "Rastreador sagaz.", "2", "3", "1", "0", "0"],
        ["6", "Pirata", "Mestre dos mares.", "2", "1", "3", "0", "0"],    
        ["7", "Druída", "Protetor da natureza.", "0", "0", "2", "2", "2"],
        ["8", "Baluarte", "É a personificação da defesa.", "1", "0", "5", "0", "0", "Guerreiro"],
        ["9", "Beserker", "O significado de força.", "5", "0", "1", "0", "0", "Guerreiro"],
        ["10", "Espada Especial", "Guerreiro versátil e poderoso.", "0", "0", "1", "0", "5", "Guerreiro"],
        ["11", "Assassino", "Matador silencioso.", "1", "4", "1", "0", "0", "Caçador"],
        ["12", "Arqueiro", "Mestre do arco e flecha.", "0", "4", "0", "2", "0", "Caçador"],
        ["13", "Envenenador", "Sábio e letal.", "0", "3", "0", "0", "3", "Caçador"],
        ["14", "Especialista Negro", "Arauto da destruição.", "0", "0", "1", "0", "5", "Especialista"],
        ["15", "Especialista Branco", "Sábio e bondoso.", "0", "0", "0", "3", "3", "Especialista"],
        ["16", "Especialista de Combate", "Gênio da arte do combate.", "2", "2", "0", "0", "2", "Especialista"],
        ["17", "Maestro", "Regente musical.", "0", "0", "0", "3", "3", "Bardo"],
        ["18", "Galante", "Sedutor e manipulador.", "0", "1", "0", "5", "0", "Bardo"],
        ["19", "Metaleiro", "Devoto da arte do rock 'n roll.", "0", "3", "0", "3", "0", "Bardo"],
        ["20", "Invocador", "Invocador de mitos.", "0", "0", "1", "5", "0", "Domador"],
        ["21", "Treinador", "Adestrador de feras.", "0", "2", "1", "3", "0", "Domador"],
        ["22", "Açogueiro", "Convocador de criaturas abatidas.", "3", "1", "0", "2", "0", "Domador"],
        ["23", "Capitão", "Líder nato.", "1", "1", "0", "4", "0", "Pirata"],
        ["24", "Terror dos Mares", "Símbolo do terror abissal.", "0", "0", "1", "0", "5", "Pirata"],
        ["23", "Almirante", "Escudeiro dos mares.", "2", "0", "4", "0", "0", "Pirata"],
        ["24", "Bestial", "Manifestação animalesca.", "2", "2", "2", "0", "0", "Druida"],
        ["23", "Protetor", "Preservador da vida.", "0", "0", "2", "2", "2", "Druida"],
        ["24", "Especialista Verde", "Manipulador de naturezas.", "0", "0", "0", "3", "3", "Druida"],
    ]
    data_model.add_data(dados_classes)

def load_estados(data_model):
    dados_estados = [
        ["1", "Normal", "Estado padrão do personagem.", "Nenhum efeito especial", "2"],
        ["2", "Envenenado", "Envenenamento afetando o personagem.", "Perda gradual de vida", "2"],
        ["3", "Atordoado", "Personagem atordoado e incapaz de agir.", "Incapacidade de ações por um turno", "2"],
        ["4", "Enraizado", "Personagem preso no lugar.", "Incapacidade de se mover por um turno", "2"],
        ["5", "Confuso", "Personagem confuso e desorientado.", "Ações imprevisíveis", "2"]
    ]
    data_model.add_data(dados_estados)

def load_itens(data_model):
    dados_itens = [
        ["1", "Poção de Cura", "Uma poção capaz de restaurar vida do alvo","2", "10", "15"],
        ["2", "Poção de Mana", "Uma poção capaz de restaurar mana do alvo", "2","10", "15"],
        ["3", "Poção de Vigor", "Uma poção capaz de restaurar vigor do alvo", "2", "10", "15"],
        ["4", "Poção de Força", "Uma poção capaz de aumentar temporariamente a força do alvo", "2", "2", "3"],
        ["5", "Poção de Agilidade", "Uma poção capaz de aumentar temporariamente a Destreza do alvo","2", "2", "3"]
    ]
    data_model.add_data(dados_itens)

def load_bolsas(data_model, data_model_personagens, data_model_itens):
    bolsas_data = []

    # Recuperar os COD's dos personagens e itens
    personagens_data = data_model_personagens.show_data().values.tolist()
    itens_data = data_model_itens.show_data().values.tolist()

    for personagem in personagens_data:
        cod_personagem = personagem[0]
        for i in range(2):  # Adicionar 2 itens aleatórios para cada personagem
            cod = len(bolsas_data) + 1
            item_escolhido = random.choice(itens_data)
            cod_item = item_escolhido[0]
            quantidade = str(random.randint(1, 5))  # Quantidade aleatória entre 1 e 5
            bolsas_data.append([str(cod), cod_personagem, cod_item, quantidade])

    data_model.add_data(bolsas_data)

def generate_random_name():
    # Gerar um nome aleatório com 6 a 10 caracteres
    length = random.randint(6, 10)
    letters = string.ascii_letters

    # Lista de vogais
    vowels = 'aeiouAEIOU'

    name = ''
    previous_is_consonant = False  # Flag para acompanhar se a última letra foi uma consoante

    for _ in range(length):
        # Escolher uma letra aleatória
        letter = random.choice(letters)
        
        # Verificar se a letra é uma consoante
        is_consonant = letter not in vowels
        
        if previous_is_consonant and is_consonant:
            # Se a última letra foi uma consoante e a letra atual é uma consoante, adicionar uma vogal
            name += random.choice(vowels)
        
        # Adicionar a letra ao nome
        name += letter
        
        # Atualizar a flag
        previous_is_consonant = is_consonant

    return name

def load_bestiario(data_model, data_model_reinos):
    bestiario_data = []

    # Recuperar os IDs dos reinos
    reinos_data = data_model_reinos.show_data().values.tolist()

    for cod in range(1, 6):  # Adicionar dados para 5 monstros fictícios
        nome = generate_random_name()
        genero = random.choice(["Masculino", "Feminino"])
        raca = "Besta"
        classe = "Monstro"
        level = str(random.randint(1, 10))
        estado = "Normal"
        vida_t = str(random.randint(50, 150))
        vida_a = vida_t
        mana_t = str(random.randint(20, 80))
        mana_a = mana_t
        vigor_t = str(random.randint(30, 100))
        vigor_a = vigor_t
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
        cod_reino = random.choice(reinos_data)[0]  # Escolha aleatória de um reino

        bestiario_data.append([str(cod), nome, genero, raca, classe, level, estado, vida_t, vida_a, mana_t, mana_a, vigor_t, vigor_a,
                               dano_fisico, dano_especial, defesa, defesa_especial, chance_esquiva,
                               forca, destreza, constituicao, carisma, inteligencia, cod_reino, "1", "1"])

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
        ["1", "6", "Olá, aventureiro! Precisa de itens para suas jornadas?", "Neutra", "Vendedor", "Neutra", "1", "1", "1"],
        ["2", "7", "Ei, você! Está pronto para enfrentar desafios?", "Boa", "Mentor", "Boa", "2", "2", "2"],
        ["3", "7", "Vai encarar meu desafio? Hahaha, boa sorte!", "Ruim", "Mentor", "Boa", "3", "3", "3"],
        ["4", "6", "Bem-vindo, aventureiro! O que você procura?", "Neutra", "Vendedor", "Neutra", "1", "1", "1"],
        ["5", "6", "Se você tem itens valiosos, estou disposto a comprá-los.", "Neutra", "Vendedor", "Neutra", "2", "2", "2"]
    ]
    
    data_model.add_data(npc_data)


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    game_data_dir = r'C:\Users\Sarakura\Desktop\Projeto\Attack_on_Ancestors\game_data'

    # Crie instâncias do DataModel para cada tabela
    data_model_reinos = DataModel(os.path.join(game_data_dir, "Reinos.csv"))
    data_model_personagens = DataModel(os.path.join(game_data_dir, "Personagens.csv"))
    data_model_racas = DataModel(os.path.join(game_data_dir, "Racas.csv"))
    data_model_classes = DataModel(os.path.join(game_data_dir, "Classes.csv"))
    data_model_estados = DataModel(os.path.join(game_data_dir, "Estados.csv"))
    data_model_itens = DataModel(os.path.join(game_data_dir, "Itens.csv"))
    data_model_bolsas = DataModel(os.path.join(game_data_dir, "Bolsas.csv"))
    data_model_bestiario = DataModel(os.path.join(game_data_dir, "Bestiario.csv"))
    data_model_atributos = DataModel(os.path.join(game_data_dir, "Atributos.csv"))
    data_model_frases_narrador = DataModel(os.path.join(game_data_dir, "Frases_Narrador.csv"))
    data_model_frases_classes = DataModel(os.path.join(game_data_dir, "Frases_Classes.csv"))
    data_model_acoes_personagens = DataModel(os.path.join(game_data_dir, "Acoes_Personagens.csv"))
    data_model_frases_npc = DataModel(os.path.join(game_data_dir, "Frases_Npc.csv"))
    
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