class Pai:
    def __init__(self, nome_pai):
        self.nome_pai = nome_pai


class Mae:
    def __init__(self, nome_mae):
        self.nome_mae = nome_mae


class Filho(Pai, Mae):
    def __init__(self, nome_pai, nome_mae, nome_filho):
        Pai.__init__(self, nome_pai)
        Mae.__init__(self, nome_mae)
        self.nome_filho = nome_filho


filho = Filho("João", "Maria", "Lucas")

print(f"Pai: {filho.nome_pai}")
print(f"Mãe: {filho.nome_mae}")
print(f"Filho: {filho.nome_filho}")