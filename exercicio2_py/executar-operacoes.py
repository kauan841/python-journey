def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def executar(funcao, a, b):
    return funcao(a, b)

resultado1 = executar(somar, 10, 20)
resultado2 = executar(multiplicar, 10, 20)

print(f"Resultado da soma: {resultado1}")
print(f"Resultado da multiplicação: {resultado2}")