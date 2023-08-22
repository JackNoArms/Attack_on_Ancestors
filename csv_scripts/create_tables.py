from data_model import DataModel
from table_model import TableModel


# PERSONAGENS
tabela = TableModel("Personagens")
colunas = ["COD", "NOME","GENERO", "RACA", "CLASSE", "LEVEL", "ESTADO", "VIDA_T","VIDA_A", "MANA_T", "MANA_A", "VIGOR_T", "VIGOR_A", "DANO_FISICO", "DANO_ESPECIAL", "DEFESA", "DEFESA_ESPECIAL", "CHANCE_ESQUIVA",
           "FORCA", "DESTREZA", "CONSTITUICAO", "CARISMA", "INTELIGENCIA", "COD_REINO", "COD_CIDADE", "COD_LOCALIDADE", "NPC"]
tabela.create_csv(columns=colunas)

# RAÇAS 25 PONTOS DIVIDOS ENTRE OS ATRIBUTOS
tabela = TableModel("Racas")
colunas = ["COD", "NOME", "DESCRICAO", "FORCA", "DESTREZA", "CONSTITUICAO", "CARISMA", "INTELIGENCIA"]
tabela.create_csv(columns=colunas)

# CLASSES 6 PONTOS DIVIDIDOS ENTRE OS ATRIBUTOS
tabela = TableModel("Classes")
colunas = ["COD", "NOME", "DESCRICAO", "FORCA", "DESTREZA", "CONSTITUICAO", "CARISMA", "INTELIGENCIA"]
tabela.create_csv(columns=colunas)

# ESTADOS
tabela = TableModel("Estados")
colunas = ["COD", "NOME", "DESCRICAO", "EFEITO", "DURACAO"]
tabela.create_csv(columns=colunas)

# ITENS
tabela = TableModel("Itens")
colunas = ["COD", "NOME", "DESCRICAO", "DURACAO", "EFEITO", "LEVEL"]
tabela.create_csv(columns=colunas)

# BOLSAS
tabela = TableModel("Bolsas")
colunas = ["COD", "COD_PERSONAGEM", "COD_ITEM", "QUANTIDADE"]
tabela.create_csv(columns=colunas)

# BESTIARIO
tabela = TableModel("Bestiario")
# Coluna TURNO é o horário do dia que o monstro SPAWNA
colunas = ["COD", "NOME","GENERO", "RACA", "CLASSE", "LEVEL", "ESTADO", "VIDA_T","VIDA_A", "MANA_T", "MANA_A", "VIGOR_T", "VIGOR_A", "DANO_FISICO", "DANO_ESPECIAL", "DEFESA", "DEFESA_ESPECIAL", "CHANCE_ESQUIVA", "FORCA", "DESTREZA", "CONSTITUICAO", "CARISMA", "INTELIGENCIA", "COD_REINO", "COD_CIDADE", "COD_LOCALIDADE"]
tabela.create_csv(columns=colunas)

# ATRIBUTOS
tabela = TableModel("Atributos")
colunas = ["COD", "NOME", "DESCRICAO", "EFEITO", "PROFICIENCIA"]
tabela.create_csv(columns=colunas)

# FRASES_NARRADOR
tabela = TableModel("Frases_Narrador")
colunas = ["COD", "FRASE", "TP_ACAO"]
tabela.create_csv(columns=colunas)

# FRASES_CLASSES
tabela = TableModel("Frases_Classes")
# A coluna frase são respostas que supostamente a classe diria em um diálogo, a coluna TP_ACOES diria se a ação é boa, ruim ou neutra
colunas = ["COD", "COD_CLASSE", "FRASE", "TP_ACAO"]
tabela.create_csv(columns=colunas) 

# ACOES_PERSONAGENS
tabela = TableModel("Acoes_Personagens")
# A coluna TP_ACOES diria se a ação é boa, ruim ou neutra
colunas = ["COD","COD_PERSONAGEM", "COD_FRASE_CLASSE", "TP_ACAO_FRASE_CLASSE"]
tabela.create_csv(columns=colunas)

# FRASES_NPC
tabela = TableModel("Frases_Npc")
# A coluna FUNCAO definiria o que o NPC faz, ex:Vendedor, Mentor(Dá missão)
# A coluna NATUREZA define se o NPC gostará de personagens que tem mais ações ruins, boas ou neutras.
colunas = ["COD", "COD_PERSONAGEM", "FRASES", "TP_ACAO", "FUNCAO", "NATUREZA", "COD_REINO", "COD_CIDADE", "COD_LOCALIDADE"]
tabela.create_csv(columns=colunas)

# Reinos
tabela = TableModel("Reinos")
colunas = ["COD", "NOME"]
tabela.create_csv(columns=colunas)

# Habilidades das classes
tabela = TableModel("H_Classes")
colunas = ["COD", "COD_CLASSE", "NOME", "DESCRICAO", "EFEITO", "DANO_FISICO", "DANO_ESPECIAL", "ESTADO", "COOLDOWN"]
tabela.create_csv(columns=colunas)

# Equipamentos 
tabela = TableModel("Equipamentos")
colunas = ["COD", "NOME", "BUFF"]
tabela.create_csv(columns=colunas)

# Habilidades de raça
tabela = TableModel("H_raca")
colunas = ["COD", "COD_RACA", "NOME", "BUFF", "DURACAO"]
tabela.create_csv(columns=colunas)

# Cidades
tabela = TableModel("Cidades")
colunas = ["COD", "COD_REINO", "NOME"]
tabela.create_csv(columns=colunas)

# Localidades
tabela = TableModel("Localidades")
colunas = ["COD", "COD_REINO", "COD_CIDADE", "NOME"] 
tabela.create_csv(columns=colunas)