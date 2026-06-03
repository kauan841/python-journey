class casa:
    def __init__(self, comodos):
        self.comodos = []


    def Adicionar_comodo(self, comodo):
        self.comodos.append(comodo)

casa1 = casa([])
casa1.Adicionar_comodo("Sala de Estar")
casa1.Adicionar_comodo("Cozinha")
casa1.Adicionar_comodo("Banheiro")
print(f"A casa tem os seguintes cômodos: {casa1.comodos}")

