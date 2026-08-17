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
print(hasattr(numeros, '__iter__'))

print(next(numeros))
print(next(numeros))
print(next(numeros))
print(next(numeros))
print(next(numeros))
