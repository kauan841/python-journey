class Pessoa:
    def __init__(self,nome):
        self.nome = nome



class Aluno(Pessoa):
  pass


c  = Pessoa("paulo")
print(c.nome)

a = Aluno("maria")
print(a.nome)
