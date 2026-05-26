def adicionar(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


lista1 = []
adicionar("Maria", lista1)
adicionar("luan", lista1)
adicionar("Marcos", lista1)
adicionar("jose", lista1)

lista2 = adicionar("Carlos")



print("Lista 1:", lista1)
print("Lista 2:", lista2)






