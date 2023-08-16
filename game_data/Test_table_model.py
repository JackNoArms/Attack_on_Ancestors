import unittest
import os
from table_model import TableModel

class TestTableModel(unittest.TestCase):

    # Cria uma instância de TableModel
    def setUp(self):
        self.test_file = "test_file.csv"
        self.table = TableModel(self.test_file)
    
    # Excluir o arquivo de teste que foi criado
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    # Testando o método "create_csv"
    def test_create_csv(self):
        columns = ["nome", "idade", "teste1"]
        self.table.create_csv(columns)
        self.assertTrue(os.path.exists(self.test_file))
    
    # Testando o método "exclude_csv"
    def test_exclude_csv(self):
        self.table.exclude_csv()
        self.assertFalse(os.path.exists(self.test_file))

    # Testando o método "modify_csv"
    def test_modify_csv(self):
        new_file_name = "new_test_file.csv"
        self.table.modify_csv(new_file_name)
        self.assertEqual(self.table.archive_name, new_file_name)
        

if __name__ == '__main__':
    unittest.main()