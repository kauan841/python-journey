def filtrar_strings(lista):
    return [item for item in lista if isinstance(item, str)]


dados = [1, "a", 2, "b", True, "c"]

resultado = filtrar_strings(dados)
print(resultado)