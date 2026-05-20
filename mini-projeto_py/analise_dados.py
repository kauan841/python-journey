
from functools import reduce

vendas = [
    {"produto": "Produto A", "preco": 150.0, "categoria": "Eletrônicos"},
    {"produto": "Produto B", "preco": 80.0, "categoria": "Roupas"},
    {"produto": "Produto C", "preco": 200.0, "categoria": "Eletrônicos"},
    {"produto": "Produto D", "preco": 50.0, "categoria": "Roupas"},
    {"produto": "Produto E", "preco": 120.0, "categoria": "Eletrônicos"},
]       

produtos_acima_100 = filter(lambda x: x["preco"] > 100, vendas)
print("Produtos acima de R$100:")
for produto in produtos_acima_100:
    print(produto["produto"])

total_vendas = reduce(lambda total, produto: total + produto["preco"], vendas, 0)
print(f"\nTotal das vendas: R${total_vendas:.2f}")
