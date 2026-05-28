def soma(a, b,/, c=0):
    return a + b + c

resultado = soma(5, 3)
print(resultado)  # Saída: 8

resultado = soma(5, 3, c=2)
print(resultado)  # Saída: 10


def subtracao(a, b,*, c):
    return a - b - c

resultado = subtracao(10, 4, c=2)
print(resultado)  # Saída: 4
