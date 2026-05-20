numero_pares = [1, 2, 3, 4, 5, 6]

def numeros_pares(x):
    return x % 2 == 0

numeros_filtrados = filter(numeros_pares, numero_pares)
print(list(numeros_filtrados))