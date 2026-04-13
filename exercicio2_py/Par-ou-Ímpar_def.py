def verificar_numero(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
numero = int(input("Digite um número inteiro: "))
resultado = verificar_numero(numero)
print(f"O número {numero} é {resultado}.")
