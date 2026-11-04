produtos = ["mouse", "teclado", "monitor", "fone"]
print("Produtos disponíveis:", produtos)

escolha = input('escolha um produto da loja:  ')

if escolha in produtos :
    print(f"muito legal esse {escolha}")
elif escolha not in produtos:
    print(f"esse {escolha} não esta disponivel na loja")
