def mostrar_usuario(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")


mostrar_usuario(nome="Kauan", idade=16, cidade="SP")