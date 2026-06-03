class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    @property
    def preco_com_desconto(self):
        return self._preco * 0.9

produto1 = Produto("Camiseta", 50)
print(f"Produto: {produto1.nome}, Preço: {produto1._preco}, Preço com desconto: {produto1.preco_com_desconto}")

