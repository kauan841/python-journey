class Aluno:
    def __init__(self,nome,idade,nota):
        self.nome = nome
        self.nota = nota
        self.idade = idade

    def apresentar(self):
        print(f'o {self.nome} tem {self.idade} anos e no total tirou essa nota em matematica {self.nota}')


Pessoa_1 = Aluno('davi',18,9)
Aluno.apresentar(Pessoa_1)

Pessoa_2 = Aluno('lucas',17,7)
Aluno.apresentar(Pessoa_2)

Pessoa_3 = Aluno('joão',16,10)
Aluno.apresentar(Pessoa_3)

        