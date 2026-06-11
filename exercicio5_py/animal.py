class Animal:
    def emitir_som(self):
        print("Som genérico")


class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")


animal1 = Cachorro()
animal1.emitir_som()