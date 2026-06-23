from abc import ABC,abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Carro(Veiculo):
    def ligar(self):
        print("Carro ligado")
    

hb20 = Carro()
hb20.ligar()