produtos = [
    {"nome": "Teclado", "preco": 150},
    {"nome": "Mouse", "preco": 50},
    {"nome": "Monitor", "preco": 900}
]

produtos_ordenados = sorted(produtos, key=lambda x: x["preco"])
for produto in produtos_ordenados:
    print(f"{produto['nome']}: R${produto['preco']}")