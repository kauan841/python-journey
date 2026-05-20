from functools import reduce

def somar_precos(total, produto):
    return total + produto["preco"]


produtos = [
    {"nome": "Produto A", "preco": 10.0},
    {"nome": "Produto B", "preco": 20.0},
    {"nome": "Produto C", "preco": 30.0},
]

preco_total = reduce(somar_precos, produtos, 0)
print(preco_total)