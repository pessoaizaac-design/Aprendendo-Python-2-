from copy import deepcopy
from pprint import pprint

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

#--------------------------------------------------------------------------

print('Exercício 22')
original2 = [
    [1.2],
    [3,4]
]

copia2 = deepcopy(original2)
copia2[0][0] = 999
print(original2)
print(copia2)

#--------------------------------------------------------------------------

# Set
print('Exercício 23')
numeros = [1, 2, 2, 3, 4, 4, 5, 5, 5]
numeros_atualizados = list(set(numeros))
print(numeros_atualizados)

#--------------------------------------------------------------------------

print('Exercício 24')
a = {1,2,3,4,5}
b = {4,5,6,7,8}

print(a | b)
print(a & b)
print(a - b)
print(b - a)

#--------------------------------------------------------------------------

# Métofos de set
print('Exercício 25')
numbers = {1, 2, 3}
numbers.add(4)
numbers.update([5,6,7])
numbers.remove(2)
numbers.discard(10)
print(numbers)

#--------------------------------------------------------------------------

print('Exercício 26')
usuarios_online = {'Higor', 'Ana', 'Carlos'}
usuarios_online.add('Pedro')
usuarios_online.discard('Ana')
print(usuarios_online)

#--------------------------------------------------------------------------

# Lambda, sort e sorted
print('Exercício 27')
numbers2 = [5, 2, 8, 1, 9, 3]
numeros_organizados = (lambda x: sorted(x))(numbers2)
print(numeros_organizados)

#--------------------------------------------------------------------------

print('Exercício 28')
pessoas = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Higor", "idade": 18},
    {"nome": "Carlos", "idade": 30}
]
idadades_organizadas = sorted(pessoas, key=lambda d: d['idade'])
print(idadades_organizadas)

#--------------------------------------------------------------------------

# Args e Kwargs
print('Exercício 29')
def informacoes(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}')

informacoes(nome='Higor',idade=18,cidade='Recife')

#--------------------------------------------------------------------------

print('Exercício 30')
def aleatorios(*args, **kwargs):
    print('--- Valores do args ---')
    for valor in args:
        print(f'{valor}')
    print('\n--- Valores do kwargs ---')
    for k,v in kwargs.items():
        print(f'{k}: {v}')

aleatorios(10,20,30,nome='Higor',linguagem='Python')

#--------------------------------------------------------------------------
# list comprehention
print('Exercício 31')
list_comprehension = [i for i in range(1,11)]
print(list_comprehension)

#--------------------------------------------------------------------------


print('Exercício 32')
numeros_s = [1,2,3,4,5]
numeros_list_comprehension = [valor * 2 for valor in numeros_s]
print(numeros_list_comprehension)

#--------------------------------------------------------------------------
# filtro em list comprehention
print('Exercício 33')
numeros_z = [1,2,3,4,5,6,7,8,9,10]
numbers_list_comprehension = list([valor for valor in numeros_z if valor % 2 == 0])
print(numbers_list_comprehension)

#--------------------------------------------------------------------------

print('Exercício 34')
idades = [12,18, 15, 21, 17, 30, 14]
idades_list_comprehension = list([idade for idade in idades if idade >= 18])
print(idades_list_comprehension)

#--------------------------------------------------------------------------
# list comprehension com mais de um for
print('Exercício 35')
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']

lista_list_comprehension = [f"{valores}{letras}" for valores in lista1 for letras in lista2]
print(lista_list_comprehension)

#--------------------------------------------------------------------------

print('Exercício 36')
matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]

matriz_list_comprehension = [valor for linha in matriz for valor in linha]
print(matriz_list_comprehension)

#--------------------------------------------------------------------------

# Dictionary Comprehension
print('Exercício 37')
list_numbers = [1 ,2 ,3, 4 ,5]

numbers_x = {value: value ** 2 for value in list_numbers}
print(numbers_x)

#--------------------------------------------------------------------------

print('Exercício 38')
names = ["Ana", "Higor", "Carlos"]

names_cont = {value: len(value) for value in names}
print(names_cont)

#--------------------------------------------------------------------------
# Set comprehension
print('Exercício 39')

numbersx = [1,2,2,3,3,4,5]

numbersx_dobro = {number: number * 2 for number in numbers_x}
print(numbersx_dobro)

#--------------------------------------------------------------------------

print('Exercício 40')

palavra = 'programacao'

letras_in_palavra = {x for x in palavra}
print(letras_in_palavra)

#--------------------------------------------------------------------------
# isinstance()
print('Exercício 41')
value = 10
print(isinstance(value, int))

#--------------------------------------------------------------------------

print('Exercício 42')
dados = [10, "Python", 3.14, True, [1,2]]
print(isinstance(dados[0], int))
print(isinstance(dados[1], str))
print(isinstance(dados[2], float))
print(isinstance(dados[3], bool))
print(isinstance(dados[4], list))

#--------------------------------------------------------------------------
# truthy and falsy
print('Exercício 43')
valores = [0, 1, "", "Python", [], [1], None, False, True]
for v in valores:
    if v:
        print('Truthy')
    else:
        print('Falsy')
    print(v)
    print('-' * 10)

#--------------------------------------------------------------------------

print('Exercício 44')

def verificar(valor):
    for v in valor:
        if v:
            print('Valor preenchido')
        else:
            print('Valor vazio')
        print(v)
        print('-' * 10)
lista_testes = [0, 1, "", "Python", [], [1], None, False, True]
verificar(lista_testes)

#--------------------------------------------------------------------------
# dir(), hasattr() and getattr()
print('Ecercício 45')
linguagem = 'Python'
pprint(dir(linguagem))
print(hasattr(linguagem, 'upper'))
print(hasattr(linguagem, 'lower'))
print(hasattr(linguagem, 'banana'))

#--------------------------------------------------------------------------

print('Exercício 46')
person = {
    "nome": "Higor",
    "idade": 18
}

this_is_name = "nome"
print(person.get(this_is_name))

#--------------------------------------------------------------------------
# iterables e iterators
print('Exercício 47')
names_new = ["Ana", "Higor",  "Carlos"]
iter_names = iter(names_new)
print(next(iter_names))
print(next(iter_names))
print(next(iter_names))

#--------------------------------------------------------------------------

print('Exercício 48')
my_iterator = iter(range(1,6))
while True:
    try:
     n = next(my_iterator)
     print(n)
    except StopIteration:
     print('Programa finalizado')
     break
#--------------------------------------------------------------------------

print('Exercício 49')
gerador = (x ** 2 for x in range(1,11))
for numero_f in gerador:
    print(numero_f)

#--------------------------------------------------------------------------

print('Exercício 50')
gerador_pares = (x for x in range(1,20) if x % 2 == 0)
for numero_p in gerador_pares:
    print(numero_p)