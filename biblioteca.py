class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

def filtrar_livros(livros, **criterios):
    def atende_criterios(livro):
        # Verifica se todos os critérios passados correspondem aos atributos do livro
        for chave, valor in criterios.items():
            if getattr(livro, chave, None) != valor:
                return False
        return True

    return [livro for livro in livros if atende_criterios(livro)]