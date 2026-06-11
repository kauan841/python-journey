class Pessoa:
    def __init__(self,nome):
        self.nome = nome



class Funcionarios(Pessoa):
   def __init__(self, nome,cargo):
       super().__init__(nome)
       self.cargo = cargo

   def Aprensentar(self):
    print(f"meu nome é {self.nome} é meu cargo será {self.cargo}")






Funcionario1 = Funcionarios("lucas","mecânico")
Funcionario1.Aprensentar()

