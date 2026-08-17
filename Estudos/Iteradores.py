# Iteraveis

import sys

lista = [0,1,2,3,4,5]
lista = iter(lista) # --> Transforma a lista em um Iterador

# next --> Serve para navegr pelos  Iteradores

#lista = list(range(1000))
print(sys.getsizeof(lista)) # --> Ver quanto de memoria consome a lista

# O for transforma a lista em um Iterador
for n in lista:
    print(n)

# Exercitando

numeros = [10, 20, 30, 40, 50]
# print(hasattr(numeros, '__iter__'))  # Retorna True (é iterável)
# print(hasattr(numeros, '__next__'))  # Retorna False (não é um iterador ainda)

# CORREÇÃO: Transforma a lista em iterador
numeros = iter(numeros) 

# print(hasattr(numeros, '__next__'))  # Agora retorna True!

# Agora o next() vai funcionar perfeitamente:
print(next(numeros))  # Imprime 10
print(next(numeros))  # Imprime 20
print(next(numeros))  # Imprime 30
print(next(numeros))  # Imprime 40
print(next(numeros))  # Imprime 50
