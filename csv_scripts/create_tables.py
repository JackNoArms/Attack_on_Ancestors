from data_model import DataModel
from table_model import TableModel


# PERSONAGENS
tabela = TableModel("Personagens")
colunas = ["COD", "NOME", "RACA", "CLASSE", "LEVEL", "ESTADO", "VIDA_T","VIDA_A", "MANA_T", "MANA_A", "VIGOR_T", "VIGOR_A", "DANO_FISICO", "DANO_ESPECIAL", "DEFESA", "DEFESA_ESPECIAL", "CHANCE_ESQUIVA",
           "FORCA", "DESTREZA", "CONSTITUICAO", "CARISMA", "INTELIGENCIA", "COD_REINO", "NPC"]
tabela.create_csv(columns=colunas)

# RAÇAS
tabela = TableModel("Racas")
colunas = ["COD", "NOME", "DESCRICAO", "HABILIDADES"]
tabela.create_csv(columns=colunas)

# CLASSES
tabela = TableModel("Classes")
colunas = ["COD", "NOME", "DESCRICAO", "HABILIDADES"]
tabela.create_csv(columns=colunas)

# ESTADOS
tabela = TableModel("Estados")
colunas = ["COD", "NOME", "DESCRICAO", "EFEITO"]
tabela.create_csv(columns=colunas)

# ITENS
tabela = TableModel("Itens")
colunas = ["COD", "NOME", "DESCRICAO", "EFEITO_+_0", "EFEITO_+_1", "EFEITO_+_2", "EFEITO_+_3"]
tabela.create_csv(columns=colunas)

# BOLSAS
tabela = TableModel("Bolsas")
colunas = ["COD_PERSONAGEM", "COD_ITEN", "QUANTIDADE"]
tabela.create_csv(columns=colunas)

# BESTIARIO
tabela = TableModel("Bestiario")
# Coluna TURNO é o horário do dia que o monstro SPAWNA
colunas = ["COD", "NOME", "RACA", "CLASSE", "LEVEL", "ESTADO", "VIDA", "MANA", "VIGOR", "DANO_FISICO", "DANO_ESPECIAL", "DEFESA", "DEFESA_ESPECIAL", "CHANCE_ESQUIVA",
           "FORCA", "DESTREZA", "CONSTITUICAO", "CARISMA", "INTELIGENCIA", "TURNO", "COD_REINO"]
tabela.create_csv(columns=colunas)

# ATRIBUTOS
tabela = TableModel("Atributos")
colunas = ["COD", "NOME", "DESCRICAO", "EFEITO", "PROFICIENCIA"]
tabela.create_csv(columns=colunas)

# FRASES_NARRADOR
tabela = TableModel("Frases_Narrador")
colunas = ["COD", "FRASES", "TP_ACOES"]
tabela.create_csv(columns=colunas)

# FRASES_CLASSES
tabela = TableModel("Frases_Classes")
# A coluna frase são respostas que supostamente a classe diria em um diálogo, a coluna TP_ACOES diria se a ação é boa, ruim ou neutra
colunas = ["COD", "COD_CLASSE", "FRASES", "TP_ACOES"]
tabela.create_csv(columns=colunas) 

# ACOES_PERSONAGENS
tabela = TableModel("Acoes_Personagens")
# A coluna TP_ACOES diria se a ação é boa, ruim ou neutra
colunas = ["COD","COD_PERSONAGEM", "COD_FRASES_CLASSES", "TP_ACOES_FRASES_CLASSES"]
tabela.create_csv(columns=colunas)

# FRASES_NPC
tabela = TableModel("Frases_Npc")
# A coluna FUNCAO definiria o que o NPC faz, ex:Vendedor, Mentor(Dá missão)
# A coluna NATUREZA define se o NPC gostará de personagens que tem mais ações ruins, boas ou neutras.
colunas = ["COD", "COD_PERSONAGEM", "FRASES", "TP_ACOES", "FUNCAO", "NATUREZA", "COD_REINO"]
tabela.create_csv(columns=colunas)

# Reinos
tabela = TableModel("Reinos")
colunas = ["COD", "NOME"]
tabela.create_csv(columns=colunas)