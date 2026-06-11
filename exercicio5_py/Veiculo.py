class Veiculo:
    def __init__(self,marca):
        self.marca = marca
    


class Carro (Veiculo):
    def __init__(self, marca,lugares):
        super().__init__(marca)
        self.lugares = lugares

    def Apresentar(self):
        print(f"sua marca de Carro é {self.marca} com disponibilidades de  {self.lugares} Lugares")




carro = Carro("Toyota", 5)
carro.Apresentar()



