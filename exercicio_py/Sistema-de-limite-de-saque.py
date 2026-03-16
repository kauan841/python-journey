LIMITE_SAQUE = 1000

try:
    valor = float(input("Digite o valor do saque: "))

    if valor > LIMITE_SAQUE:
        print("Erro: limite de saque excedido")
    else:
        print("Saque realizado com sucesso")

except ValueError:
    print("Erro: valor inválido")