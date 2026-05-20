numeros = [2, 3, 4, 5]

def quadrado(x):
    return x ** 2

numeros_quadrados = map(quadrado, numeros)
print(list(numeros_quadrados))

