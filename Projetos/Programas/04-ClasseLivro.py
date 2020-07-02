class Livro:

    def __init__(self, titulo, autor, editora, isbn, ano):
        self.__titulo = titulo
        self.autor = autor
        self.editora = editora
        self.isbn = isbn
        self.ano = ano

    def __str__(self):
        return 'Titulo: %s, Autor: %s, Editora: %s, ISBN: %s, Ano: %s' % \
                (self.__titulo, self.autor, self.editora, self.isbn, self.ano)

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo


Livro1 = Livro('Curso de Python em 6h', 'Alcimar Costa', 'Udemy', '878-98-9988-988-9', 2018)

print(Livro1)
print(Livro1.titulo)
print(Livro1.autor)
print(Livro1.editora)
print(Livro1.isbn)
print(Livro1.ano)

livro1 = Livro('Curso de Python em 6h','Alcimar Costa', 'Udemy', '878-98-9988-988-9', 2018)
livro2 = Livro('Python para web', 'Alcimar Costa', 'Udemy', '999-99-999-9999-9', 2018)
livro3 = Livro('Inteligência Artificial', 'Alcimar Costa', 'Udemy', '888-88-8888-88', 2018)

livros = [livro1, livro2, livro3]

for l in livros:
    print(l)

print(livro1.autor)
print(livro1.titulo)
livro1.titulo = 'Novo titulo'
print(livro1.titulo)

