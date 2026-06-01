class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"nome: {self.nome}\nidade: {self.idade}")

pessoa1 = Pessoa("Alice", 30)
pessoa1.apresentar()  

pessoa2 = Pessoa("Bob", 25)
pessoa2.apresentar()  

