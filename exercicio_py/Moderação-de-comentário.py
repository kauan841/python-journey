comentario = input("Digite um comentário: ")

if ("Ruim" in comentario) or ("ruim" in comentario):
    print("Comentário bloqueado")
else:
    print("Comentário aprovado")