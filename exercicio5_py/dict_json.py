import json

CAMINHO_ARQUIVO = "C:\\Users\\kaike\\Desktop\\pasta_de_exercicio\\exercicio5_py\\usuarios.json"


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Helena', 21)
p2 = Pessoa('Maria', 25)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), p2.__dict__, vars(p3)]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, "w") as arquivo:
        json.dump(bd, arquivo, indent=4)

if __name__ == "__main__":
    print("Criando arquivo JSON...")
    fazer_dump()    