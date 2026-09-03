# Revendo Pythhon intermediário 4
from itertools import *
from functools import reduce


# Zip() and Zip Longest()
print('Exercício 69')
nomes = ['Higor', 'Ana', 'Carlos']
idades = [18, 20, 25]

uniao = dict(zip(nomes, idades))
print(uniao)
#-----------------------------------------------------------------------------

print('Exercício 70')
nomes1 = ['Higor', 'Ana', 'Carlos']
idades1 = [18, 20]


uniao1 = dict(zip_longest(nomes1, idades1, fillvalue='Idade não informada'))
print(uniao1)

#-----------------------------------------------------------------------------
# Itertools count
print('Exercícip 71')
for i in count(10):
    print(f'Prosseguindo {i}...')
    if i == 10:
        break

#-----------------------------------------------------------------------------

print('Exercício 72')
for i in count(0, 5):
    print(i)
    if i == 25:
        break

#-----------------------------------------------------------------------------
# combinations
print('Exercício 73')
frutas = ["maçã", "banana", "uva", "laranja"]
combinacoes_frutas = list(combinations(frutas, 2))
print(combinacoes_frutas)

#-----------------------------------------------------------------------------

print('Exercício 74')
numbers = [1, 2, 3, 4]
combinacoes_numbers = list(combinations(numbers, 3))
print(combinacoes_numbers)

#-----------------------------------------------------------------------------

# permutations
print('Exercício 75')
letras = ['A', 'B', 'C']
permutacoes = list(permutations(letras))
print(permutacoes)

#-----------------------------------------------------------------------------

print('Exercício 76')
numeros2 = [1, 2, 3]
permutacoes_numeros = list(permutations(numeros2))
print(permutacoes_numeros)

#-----------------------------------------------------------------------------

# product
print('Exercício 77')
cores = ['preto', 'branco']
tamanho = ['P', 'M', 'G']
possibilidades = list(product(cores, tamanho))
print(possibilidades)

#-----------------------------------------------------------------------------

print('Exercício 78')
senhas = ['A', 'B']
numbers1 = [1,2,3]
possibilidades_senhas = list(product(senhas, numbers1))
print(possibilidades_senhas)

#-----------------------------------------------------------------------------

# groupby
print('Exercício 79')
pessoas = [
    {'nome': 'Ana', 'cidade': 'Recife'},
    {'nome': 'Higor', 'cidade': 'Recife'},
    {'nome': 'Carlos', 'cidade': 'Olinda'},
    {'nome': 'João', 'cidade': 'Olinda'},
]

pessoas.sort(key=lambda x: x['cidade'])
for key, values in groupby(pessoas,key=lambda x: x['cidade']):
    print(f'Cidade: {key}')
    for pessoa in values:
        print(f'  -{pessoa['nome']}')
#-----------------------------------------------------------------------------

print('Exercício 80')
nums = [1,1,1,2,2,3,3,3]
for chave,valores in groupby(nums):
    print(f'Número: {chave} | Repetições: {list(valores)}')

#-----------------------------------------------------------------------------

# map
print('Exercício 81')
nums1 = [1,2,3,4,5]
nums_dobrados = list(map(lambda x: x*2, nums1)) 
print(nums_dobrados)

#-----------------------------------------------------------------------------

print('Exercício 82')
names = ['higor', 'ana', 'carlos']
names_upper = list(map(lambda x: x.upper(), names))
print(names_upper)

#-----------------------------------------------------------------------------

# partial

#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------

# filter
print('Exercício 85')
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_pares = list(filter(lambda x: x % 2 == 0, nums2))
print(num_pares)

#-----------------------------------------------------------------------------

print('Exercício 86')
ids = [12, 18, 15, 21, 30, 14, 25]
maioridade = list(filter(lambda x: x >= 18, ids))
print(maioridade)

#-----------------------------------------------------------------------------

# reduce
print('Exercício 87')
ns = [1, 2, 3, 4, 5]
soma_total = reduce(lambda soma, p: soma + p, ns, 0)
print(soma_total)

#-----------------------------------------------------------------------------

print('Exercício 88')
ns2 = [2, 3, 4]
mutiplicar = reduce(lambda mutiplos, p: mutiplos * p, ns2)
print(mutiplicar)

#-----------------------------------------------------------------------------
