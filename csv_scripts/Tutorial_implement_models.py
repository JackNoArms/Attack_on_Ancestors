from table_model import TableModel
from data_model import DataModel

tabela = TableModel("personagem.csv")
colunas = ["COD", "NOME", "VIDA"]
tabela.create_csv(columns=colunas)

adc_dados = DataModel(tabela.get_archive_name)
dados = [["1", "Lucas", "100"],
         [ "2", "Victor", "50"],
         ["3", "Mateus", "60"],
         ["4", "Stanley", "70"]]

adc_dados.add_data(dados)
adc_dados.show_data()

adc_dados.delete_data(2)
adc_dados.show_data()

mod_dados = ["1", "Victor", "50"]
adc_dados.modify_data(1,data=mod_dados)
adc_dados.show_data()

mod_dados = ["120"]
adc_dados.modify_data(1,data=mod_dados, column="VIDA")
adc_dados.show_data()
