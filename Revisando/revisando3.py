from functools import *
from itertools import *
#-----------------------------------------------------------------------------------------
# cycle()
print('Exercício 1')

colors = cycle(['Vermelho','Verde','Azul'])
count = 0

for color in colors:
    print(color)
    count += 1
    if count == 10:
        break
#-----------------------------------------------------------------------------------------

# repeat()
print('Exercício 2')
numbers = repeat(5,7)
numbers_quadrado = list(map(lambda x: x**2, numbers))
print(numbers_quadrado)
#-----------------------------------------------------------------------------------------

# accumulate()
print('Exercício 3')
numeros = [5, 10, 3, 7]
numeros_acumulados = list(accumulate(numeros))
print(numeros_acumulados)
#-----------------------------------------------------------------------------------------

# chain()
print('Exercício 4')
python = ['for', 'while', 'if']
poo = ['class', 'self', 'super']
python_poo = list(chain(python, poo))
print(python_poo)
#-----------------------------------------------------------------------------------------

# compress()
print('Exercício 5')
alunos = ['Higor', 'Pedro', 'Rafaela', 'João']
aprovados = [True, False, True, False]
alunos_aprovados = list(compress(alunos, aprovados))
print(alunos_aprovados)
#-----------------------------------------------------------------------------------------

# product()
print('Exercício 6')
cores = ['Preto', 'Branco']
tamanho = ['P', 'M', 'G']
pay = list(product(tamanho, cores))
print(pay)
#-----------------------------------------------------------------------------------------

# combinations()
print('Exercício 7')
students = ['Higor', 'Pedro', 'Rafaela', 'João']
print(list(combinations(students, r=2)))
#-----------------------------------------------------------------------------------------

# permutations()
print('Exercício 8')
letters = ['A', 'B', 'C']
print(list(permutations(letters, r=2)))
#-----------------------------------------------------------------------------------------

# singledispatch
@singledispatch
def mostrar_dado(arg):
    pass

@mostrar_dado.register
def _(arg: int):
    print(f'Inteiro: {arg}')

@mostrar_dado.register
def _(arg: str):
    print(f'Texto: {arg}')

@mostrar_dado.register
def _(arg: list):
    print(f'Lista com {len(arg)} elementos')

mostrar_dado(10)
mostrar_dado('Python')
mostrar_dado([1,2,3])
#-----------------------------------------------------------------------------------------

# partial
def multiplicador( number, multiplicator):
    return number * multiplicator

dobro = partial(multiplicador, multiplicator=2)
triplo = partial(multiplicador, multiplicator=3)

print(dobro(5))
print(triplo(5))