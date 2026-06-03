class casa:
    def __init__(self, comodos):
        self.comodos = comodos

class comodo:
    def __init__(self, nome):
        self.nome = nome

sala = comodo("Sala de Estar")
cozinha = comodo("Cozinha")
banheiro = comodo("Banheiro")

casa1 = casa([sala, cozinha, banheiro])

print(f"A casa tem os seguintes cômodos: {[comodo.nome for comodo in casa1.comodos]}")
