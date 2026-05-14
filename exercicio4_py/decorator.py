def meu_decorator(func):
    def wrapper(*args, **kwargs):
        print("Antes de chamar a função")
        func(*args, **kwargs)
        print("Depois de chamar a função")
    return wrapper

@meu_decorator
def minha_funcao():
    print("Esta é a minha função")

minha_funcao()