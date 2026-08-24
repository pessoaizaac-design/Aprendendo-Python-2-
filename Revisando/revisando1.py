from functools import reduce
from pprint import pprint
import time
import re

# Map
print("Exercício 1")
precos = [100, 250, 80, 400, 50]

precos_atualizados = list(map(lambda x: round(x * 1.10, 2), precos))
print(precos_atualizados)
print('=' * 70)
print('Exercício 2')
nomes = ["higor", "ana", "carlos", "pedro"]

letras_maiusculas = list(map(lambda nome: nome.upper(), nomes))
print(letras_maiusculas)
print('=' * 70)
# Filter
print('Exercício 3')
numbers = [4, 7, 10, 13, 20, 25, 30, 33, 40]

numeros_maiores_dez = list(filter(lambda numeros: numeros > 10 and numeros % 2 == 0, numbers))
print(numeros_maiores_dez)
print('=' * 70)
print('Exercício 4')
usuarios = [
    {"nome": "Higor", "idade": 18, "ativo": True},
    {"nome": "Ana", "idade": 22, "ativo": False},
    {"nome": "Carlos", "idade": 25, "ativo": True},
    {"nome": "Pedro", "idade": 16, "ativo": True}
]

maiores_de_idade = list(filter(lambda id: id['idade'] >= 18 and id['ativo'] == True, usuarios))
print(maiores_de_idade)
print('=' * 70)
# Reduce
print('Exercício 5')
numeros2 = [2, 3, 4, 5]

numeros_mutiplicados = reduce(lambda mutiplicar, numbers: mutiplicar * numbers, numeros2)
print(numeros_mutiplicados)
print('=' * 70)
print('Exercício 6')
notas = [8, 7, 10, 9, 6]

soma_das_notas = reduce(lambda soma, numeros: soma + numeros, notas, 0)
print(soma_das_notas)
print(f'{soma_das_notas / len(notas)}')
print('=' * 70)
# Generator
print('Exercício 7')
def numeros_impares(limite):
    for n in range(1, limite + 1):
        if n % 2 != 0:
            yield n

teste = numeros_impares(10)
for v in teste:
    pprint(v)
print('=' * 70)
print('Exercício 8')

def nomes_escolhidos(name):
    for letra in name:
        yield letra

for letra in nomes_escolhidos('Higor'):
    print(letra)
print('=' * 70)
# Iteradores
print('Exercício 9')
frutas = ["Maçã", "Banana", "Uva", "Manga"]

pecorrer_frutas = iter(frutas)
while True:
    try:
        print(next(pecorrer_frutas))
    except:
        StopIteration
        break
print('=' * 70)
print('Exercício 10')
class ContadorPares:
    
    def __init__(self,limite):
        self.limite = limite
        self.atual = 0
            

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual > self.limite:
            raise StopIteration

        resultado = self.atual
        self.atual += 2

        return resultado
contador = ContadorPares(10)
for num in contador:
    print(num)
print('=' * 70)    
# Decorator
print('Exercício 11')
def mostras_resultado(funcao):
    def wrapper(n1,n2):
        print('CALCULANDO....')
        funcao(n1,n2)
        print(f'A SOMA É IGUAL A: {n1 + n2}')
    return wrapper

@mostras_resultado
def soma(a,b):
    return a + b

soma(10, 5)
print('=' * 70)
print('Exercício 12')
def calcular_tempo(funcao):
    def wrapper(n1, n2):
        tempo_inicial = time.time()
        funcao(n1, n2)
        tempo_final = time.time()
        print(f'A duração foi de {tempo_final - tempo_inicial:.6f} segundos')
    return wrapper

@calcular_tempo
def calcular_potencia(n1, n2):
    print(f'{n1} elevado a {n2} é igual a: {n1**n2}')
    return n1 ** n2

calcular_potencia(2,2)
print('=' * 70)
# Args
print('Exercício 13')
def somar_numeros(*args):
    total =0
    for valor in args:
        total += valor
    print(total)

somar_numeros(10, 20, 30, 40)
print('=' * 70)

print('Exercício 14')
def maior_menor(*args):
    if not args:
        return None, None
    
    maior = args[0]
    menor = args[0]

    for numero in args:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero
    return maior, menor

resultado_maior, resultado_menor = maior_menor(10, 50, 3, 80, 20)
print(f"Maior: {resultado_maior}, Menor: {resultado_menor}")

print('=' * 70)
# Kwars
print('Exercício 15')
def exibir_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

exibir_dados(
    nome="Higor",
    idade=18,
    curso="CC"
)
print('=' * 70)

print('Exercício 16')
def filtrar_str(**kwargs):
    for chave, valor in kwargs.items():
        if isinstance(valor,str):
            print(f'{chave}: {valor}')

filtrar_str(
    nome="Higor",
    idade=18,
    curso="CC",
    ativo=True,
    cidade="Recife"
)
print('=' * 70)

# Import OS
print('Exercício 17')
texto = "Tenho 18 anos, moro no número 250 e meu código é 98432."

print(re.findall(r'\d+', texto))
print('=' * 70)
print('Exercício 18')
emails = [
    "higor@gmail.com",
    "teste@hotmail.com",
    "email-invalido",
    "usuario123@yahoo.com",
    "abc@",
    "pessoa@outlook.com"
]

validos = [
    email for email in emails
    if re.fullmatch(r'[\w.-]+@[\w.-]+\.\w+', email)
]

print(validos)
print('=' * 70)

# List Comprehension
print('Exercício 19')
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares_elevados = [numero ** 2 for numero in numeros if numero % 2 == 0]
print(numeros_pares_elevados)
print('=' * 70)

print('Exercício 20')
nomes = ["higor", "ana", "carlos", "joao", "maria", "pedro"]

nomes_com_quatro_ou_mais_letras = [letra.upper() for letra in nomes if isinstance(letra, str) and len(letra) > 4]
print(nomes_com_quatro_ou_mais_letras)

