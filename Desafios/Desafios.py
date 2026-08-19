from functools import reduce
from pprint import pprint

# Map

print('Desafio 1 Map')
valores = [10, 25, 50, 100, 200]

novos_valores = list(map(lambda p: p * 0.10, valores))
print(novos_valores) # Aplica 90% de desconto aos valores informados

print('=' * 70)

print('Desafio 2 Map') 
numeros1 = [2, 5, 10, 15, 20]

dobrar_valores = list(map(lambda x: x * 2, numeros1))
print(dobrar_valores) # Dobra todosos números da lista acima

print('=' * 70)

print('Desafio 3 Map')
precos = [100, 250, 500, 1000]

desconto_precos = list(map(lambda d: d * 0.90, precos))
print(desconto_precos) # Aplica 10% de desconto a todos os preços

print('=' * 70)

# Filter

print('Desafio 1 Filter')
idades = [12, 17, 18, 21, 15, 30, 16, 25]

maiores = list(filter(lambda id: id >= 18, idades))
print(maiores) # Separa os que ssão maiores de idade

print('=' * 70)

print('Desafio 2 Filter')
numeros2 = [3, 8, 11, 20, 25, 32, 41, 50]

numeros_pares = list(filter(lambda p: p % 2 == 0, numeros2))
print(numeros_pares) # Filtra os números pares da lista

print('=' * 70)

# Reduce

print('Desafio 1 Reduce')
numeros3 = [5, 10, 15, 20]

total = reduce(lambda soma, valores: soma + valores, numeros3, 0 )
print(total) # A soma de todos os valores

print('=' * 70)

print('Desafio 2 Reduce')
precos2 = [29.90, 15.50, 100, 45.90]

valor_a_pagar = reduce(lambda soma, valor: soma + valor, precos2, 0 )
print(valor_a_pagar) # Retorna o valor correto

print('=' * 70)

# Iteradores

print('Desafio 1 Iteradores')
nomes = ['Higor', 'João', 'Pedro', 'Lucas']
nomes_atualizados = iter(nomes)

print(hasattr(nomes_atualizados, '__next__')) # Retorna True

print('=' * 70)

print('Desafio 2 Iteradores')
numeros4 = [10, 20, 30, 40]
numeros_atualizados = iter(numeros4)

print(hasattr(numeros_atualizados, '__next__')) # Retorna True

print('=' * 70)

# Generators

print('Desafio 1 Generators')

def contagem():
    for n in range(1, 6):
        yield n

gerador = contagem()
print(next(gerador))

print('=' * 70)

print('Desafio 2 Generators')

def numeros_pares():
    for v in range(0,21):
        if v % 2 == 0:
            yield v

generator = numeros_pares()
for n in generator:
    pprint(n)

print('=' * 70)

# Decorator

print('Desafio 1 Decorator')


def contador(funcao):
    s = 0
    def wrapper():
        nonlocal s
        funcao()
        s +=1
        print(f'A função foi executada {s} vez(es)!')
    return wrapper

@contador
def ola():
    print('Olá!')

ola()
ola()
ola()

print('=' * 70)

print('Desafio 2 Decorator')

def mensagem(funcao):
    def wrapper():
        print('Iniciando função...')
        funcao()
        print('Função finalizada!')
    return wrapper

@mensagem
def calculando():
    print('Calculando...')

gp = calculando()
print(gp)
