class MeuErro(Exception):
    pass

try:
    raise MeuErro("Ocorreu um erro personalizado!")
except MeuErro as e:
    print(f"Erro capturado: {e}")