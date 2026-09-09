
print('Exercício 1')

class Contador:
    def __init__(self,start,end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value +=1
        return current

nums = Contador(1,5)
for num in nums:
    print(num)

#-----------------------------------------------------------------------------------------

print('Exercício 2')

class Inverso:
    def __init__(self, lista):
        self.lista = lista
        self.indice = len(lista) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice >=0:
           elemento = self.lista[self.indice]
           self.indice -=1
           return elemento

        raise StopIteration

lista = [10, 20, 30, 40]

for numero in Inverso(lista):
    print(numero)

#-----------------------------------------------------------------------------------------

print('Exercício 3')

class Pares:
    def __init__(self, inicio, fim):
        self.valor = inicio
        self.fim = fim

    def __iter__(self):
        return self

    def __next__(self):
        while self.valor < self.fim:
          atual = self.valor
          self.valor += 1

          if atual % 2 == 0:
              return atual

#-----------------------------------------------------------------------------------------

print('Exercício 4')

class Palavras:
    def __init__(self, comeco):
        self.valor = comeco.split()
        self.indice = 0
        

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice >= len(self.valor):
            raise StopIteration
        
        current = self.valor[self.indice]
        self.indice +=1

        return current


frase = 'Python é legal'
for palavra in Palavras(frase):
    print(palavra)

#-----------------------------------------------------------------------------------------

print('Exercício 5')

class Filtro:
    def __init__(self, lista, filtro):
        self.lista = lista
        self.filtro = filtro
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.indice  < len(self.lista):
            current = self.lista[self.indice]
            self.indice += 1

            if self.filtro(current):
                return current

        raise StopIteration

numeros = [1, 2, 3, 4, 5, 6]

pares = Filtro(numeros, lambda x: x % 2 == 0)

for numero in pares:
    print(numero)

#------------------------------------------------------------------------------------------

print('Exercício 6')
def contar(n):
    count = 1
    while count <= n:
        yield count
        count +=1

for numero in contar(5):
    print(numero)

#------------------------------------------------------------------------------------------

print('Exercício 7')
def pares(n):
    count = 0
    while count <= n:
        if count % 2 == 0:
            yield count
        count +=1

for numero in pares(10):
    print(numero)

#------------------------------------------------------------------------------------------

print('Exercício 8')
def quadrados(lista):
    count = 0
    while count <= len(lista) - 1:
         yield lista[count] ** 2
         count +=1

numbers = [1, 2, 3, 4]
for n in quadrados(numbers):
    print(n)

#------------------------------------------------------------------------------------------

print('Exercício 9')
def contador_infinito(inicio=1):
    numero = inicio
    while True:
        yield numero
        numero += 1

# Inicializando o gerador
numeros = contador_infinito()

# Pegando os valores sob demanda com a função next()
print(next(numeros))  # Saída: 1
print(next(numeros))  # Saída: 2
print(next(numeros))  # Saída: 3

#------------------------------------------------------------------------------------------

print('Exercício 10')
def fibonacci(n):
    count = 1
    a, b = 0, 1
    while count <= n:
        yield a
        a, b = b, a + b
        count += 1

for x in fibonacci(10):
    print(x)
