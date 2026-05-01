lista = ['python', 'java', 'c++']
iterador = iter(lista)

print(next(iterador))  # Saída: 'python'
print(next(iterador))  # Saída: 'java'
print(next(iterador))  # Saída: 'c++'
print(next(iterador))  # Levanta StopIteration, pois não há mais elementos