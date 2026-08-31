from copy import deepcopy

# Revendo python intermédiario 2

# Shallow copy
print('Exercício 21')
original = [
    [1,2],
    [3,4]
]
copia = original.copy()
copia[0][0] = 999
print(original)
print('=' * 70)

print('Exercício 22')
original2 = [
    [1.2],
    [3,4]
]

copia2 = deepcopy(original2)
copia2[0][0] = 999
print(original2)
print(copia2)
print('=' * 70)

# Set
print('Exercício 23')
numeros = [1, 2, 2, 3, 4, 4, 5, 5, 5]
numeros_atualizados = list(set(numeros))
print(numeros_atualizados)
print('=' * 70)

print('Exercício 24')
a = {1,2,3,4,5}
b = {4,5,6,7,8}

print(a | b)
print(a & b)
print(a - b)
print(b - a)
print('=' * 70)

# Métofos de set
print('Exercício 25')
numbers = {1, 2, 3}
numbers.add(4)
numbers.update([5,6,7])
numbers.remove(2)
numbers.discard(10)
print(numbers)
print('=' * 70)

print('Exercício 26')
usuarios_online = {'Higor', 'Ana', 'Carlos'}
usuarios_online.add('Pedro')
usuarios_online.discard('Ana')
print(usuarios_online)
print('=' * 70)

# Lambda, sort e sorted
print('Exercício 27')
numbers2 = [5, 2, 8, 1, 9, 3]
numeros_organizados = (lambda x: sorted(x))(numbers2)
print(numeros_organizados)
print('=' * 70)

print('Exercício 28')
pessoas = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Higor", "idade": 18},
    {"nome": "Carlos", "idade": 30}
]
idadades_organizadas = sorted(pessoas, key=lambda d: d['idade'])
print(idadades_organizadas)
print('=' * 70)

# Args e Kwargs
print('Exercício 29')
def informacoes(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}')

informacoes(nome='Higor',idade=18,cidade='Recife')
print('=' * 70)

print('Exercício 30')
def aleatorios(*args, **kwargs):
    print('--- Valores do args ---')
    for valor in args:
        print(f'{valor}')
    print('\n--- Valores do kwargs ---')
    for k,v in kwargs.items():
        print(f'{k}: {v}')

aleatorios(10,20,30,nome='Higor',linguagem='Python')