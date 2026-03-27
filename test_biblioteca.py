import unittest
from biblioteca import Livro, filtrar_livros

class TestFiltroLivros(unittest.TestCase):
    def setUp(self):
        # Base de dados simulada para os testes
        self.biblioteca = [
            Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954),
            Livro("O Hobbit", "J.R.R. Tolkien", 1937),
            Livro("1984", "George Orwell", 1949)
        ]

    def test_deve_filtrar_livros_por_autor(self):
        resultado = filtrar_livros(self.biblioteca, autor="J.R.R. Tolkien")
        
        self.assertEqual(len(resultado), 2)
        self.assertEqual(resultado[0].titulo, "O Senhor dos Anéis")
        self.assertEqual(resultado[1].titulo, "O Hobbit")

    def test_deve_filtrar_livros_por_ano(self):
        resultado = filtrar_livros(self.biblioteca, ano=1949)
        
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0].titulo, "1984")

# Esse bloco no final permite rodar o teste direto no VS Code
if __name__ == '__main__':
    unittest.main()