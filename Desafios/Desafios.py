from functools import reduce
from pprint import pprint
import time

# Map

print('Desafio 1 Map')
produtos = [
    {"nome": "Mouse", "preco": 80},
    {"nome": "Teclado", "preco": 150},
    {"nome": "Monitor", "preco": 900},
    {"nome": "Headset", "preco": 250}
]

quinze_desconto = list(map(lambda produto: produto['preco'] * 0.85, produtos))
print(quinze_desconto)

print('=' * 70)

print('Desafio 2 Map')
usuarios = [
    ("Higor", 18),
    ("Carlos", 22),
    ("Ana", 17),
    ("Pedro", 25)
]

frase_user = list(map(lambda x: f'{x[0]} tem {x[1]} anos', usuarios)) # Lembrar da contagem de elementos da lista
print(frase_user)

print('=' * 70)

# Filter

print('Desafio 1 Filter')
usuarios2 = [
    {"nome": "Higor", "idade": 18, "ativo": True},
    {"nome": "Carlos", "idade": 15, "ativo": False},
    {"nome": "Ana", "idade": 22, "ativo": True},
    {"nome": "Pedro", "idade": 17, "ativo": True}
]

maior_de_idade = list(filter(lambda id: id['idade'] >= 18, usuarios2))
print(maior_de_idade)

print('=' * 70)

print('Desafio 2 Filter')
numeros = []
for n in  range(0,101):
    numeros.append(n)

divisiveis_maiores = list(filter(lambda ns: ns % 3 == 0 and ns % 5 != 0 and ns > 20, numeros))
print(divisiveis_maiores)

print('=' * 70)

# Reduce

print('Desafio 1 Reduce')
numeros2 = [15, 42, 7, 89, 34, 61, 3]

maior_numero = reduce(lambda a, b: a if a > b else b, numeros2)
print(maior_numero)

print('=' * 70)

print('Desafio 2 Reduce')
compras = [
    {"produto": "Mouse", "preco": 80},
    {"produto": "Teclado", "preco": 150},
    {"produto": "Headset", "preco": 200},
    {"produto": "Monitor", "preco": 900}
]

total_a_pagar = reduce(lambda soma, preco: soma + preco['preco'], compras, 0)
print(total_a_pagar)

print('=' * 70)

# Generator
print('Desafio 1 Generator')
def pares(limite):
    for n in range(0, limite + 1):
        if n % 2 == 0:
            yield(n)

gag = pares(10)
for numeros in gag:
    print(numeros)

print('=' * 70)

print('Desafio 2 Generator')
def fibonacci_gen(limite):
    a, b = 0, 1
    for _ in range(limite):
        yield a
        a, b = b, a + b

# Consumindo o gerador
#for num in fibonacci_gen(10):
    #print(num, end=" "\n)

print('=' * 70)

# Iteradores

print('Desafio 1 Iteradores')
nomes = ["Higor", "Ana", "Carlos", "Pedro"]

nomes_atualizados = iter(nomes)
print(next(nomes_atualizados))

print('=' * 70)

print('Desafio 2 Iteradores')
class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.numero = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.numero <= self.limite:
            valor = self.numero
            self.numero += 1
            return valor
        raise StopIteration


contador = Contador(5)

for numero in contador:
    print(numero)


print('=' * 70)

# Decorator

print("Desafio 1 Decorator")
def contagem_tempo(funcao):
    def wrapper():
        t1 = time.time()
        funcao()
        t2 = time.time()
        print(f'A duração foi de {t2 - t1:.6f} segundos')
    return wrapper

@contagem_tempo
def soma():
    total = 0
    for i in range(1_000_000):
        total += i
    return total

print(soma())




        