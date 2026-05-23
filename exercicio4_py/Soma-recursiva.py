n = [1, 2, 3, 4]
def soma_recursiva(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_recursiva(lista[1:])
resultado = soma_recursiva(n)
print(resultado)
        