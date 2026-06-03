class pessoa:
    total_pessoas = 0
    def __init__(self, pessoas):
        self.pessoas = pessoas
        pessoa.total_pessoas += 1

pessoa1 = pessoa("pessoa1")
pessoa2 = pessoa("pessoa2")
print("Total de pessoas:", pessoa.total_pessoas)


