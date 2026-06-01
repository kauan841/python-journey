class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_produto(self):
        print(f"Produto: {self.nome}\nPreço: R${self.preco}")

produto1 = Produto("Notebook", 2500)
produto1.mostrar_produto()
     