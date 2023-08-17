# Importando a classe TableModel
from table_model import TableModel

# Criando uma instância da classe TableModel
table = TableModel("dados.csv")

# Exemplo de uso do método create_csv
columns = ["cod", "nome", "idade"]
table.create_csv(columns)  # Cria um arquivo CSV com as colunas fornecidas

# Exemplo de uso do método exclude_csv
table.exclude_csv()  # Exclui o arquivo CSV, se existir

# Exemplo de uso do método modify_csv
new_file_name = "novo_arquivo.csv"
table.modify_csv(new_file_name)  # Modifica o nome do arquivo CSV
