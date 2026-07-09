class Animal:
    def emitar_som(self):
        pass

class Cachorro(Animal):
   def emitar_som(self):
       print('AU AU AU')

class Gato(Animal):
   def emitar_som(self):
       print('MIAU MIAU MIAU')


class Vaca(Animal):
   def emitar_som(self):
       print('MU MU MU')



animais = [Cachorro(), Gato(), Vaca()]

for animal in animais:
    animal.emitar_som()
