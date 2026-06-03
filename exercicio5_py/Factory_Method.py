class usuario:
    def __init__(self, nome):
        self.nome = nome

    @classmethod
    def criar_admin(cls, nome):
        return cls(nome)

pessoa1 = usuario.criar_admin("maria")
print(pessoa1.nome)