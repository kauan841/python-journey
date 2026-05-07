def quadrados(n):
    for i in range(n):
        yield i ** 2
for numero in quadrados(10):
    print(numero)