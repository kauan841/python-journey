from abc import ABC, abstractmethod

class Operacao(ABC):

    @abstractmethod
    def calcular(self, a, b):
        pass

class Soma(Operacao):
    def calcular(self, a, b):
        return a + b
    
class Subtracao(Operacao):
    def calcular(self,a,b):
        return a - b
    
class Multiplicacao(Operacao):
    def calcular(self,a,b):
        return a * b 
    

teste1 = Soma()
teste2 = Subtracao()
teste3 = Multiplicacao()


print(teste1.calcular(5,100))
print(teste2.calcular(105,100))
print(teste3.calcular(5,100))