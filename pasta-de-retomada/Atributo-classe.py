class Pessoa:
    total_pessoas = 0

    def __init__(self):
        Pessoa.total_pessoas += 1


primeira_pessoa = Pessoa()
segunda_pessoa = Pessoa()
terceira_pessoa = Pessoa()
quarta_pessoa = Pessoa()
quinta_pessoa = Pessoa()

print(f'Total de pessoas: {Pessoa.total_pessoas}')