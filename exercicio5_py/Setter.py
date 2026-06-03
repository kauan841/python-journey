
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = valor

    @property
    def preco_com_desconto(self):
        return self._preco * 0.9


produto1 = Produto("Camiseta", 50)

print(f"Produto: {produto1.nome}")
print(f"Preço: R${produto1.preco}")
print(f"Preço com desconto: R${produto1.preco_com_desconto}")