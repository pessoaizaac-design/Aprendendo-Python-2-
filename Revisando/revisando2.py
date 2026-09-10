print('Revisão 1')
class Contador:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

contador = Contador(1,5)
for n in contador:
    print(n)
#------------------------------------------------------------------------------------------

print('Revisão 2')
class Pares:
    def __init__(self, final):
        self.final = final
        self.inicio = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.inicio > self.final:
            raise StopIteration
        atual = self.inicio
        self.inicio += 2
        return atual


for n in Pares(6):
    print(n)
#------------------------------------------------------------------------------------------

print('Revisão 3')
class ContagemRegressiva:
    def __init__(self, valor):
        self.valor = valor
        self.inicio = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.valor < self.inicio:
            raise StopIteration
        atual = self.valor
        self.valor -= 1
        return atual
    
for n in ContagemRegressiva(5):
    print(n)
#------------------------------------------------------------------------------------------

print('Revisão 4')
class IteradorDePalavras:
    def __init__(self,lista):
        self.lista = lista
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice > len(self.lista) - 1:
            raise StopIteration 
        atual = self.lista[self.indice]
        self.indice += 1
        return atual

palavras = IteradorDePalavras(['Python', 'Java', 'C++'])
for p in palavras:
    print(p)
#------------------------------------------------------------------------------------------

print('Revisão 5')
class Multiplos:
    def __init__(self, inicial, final, multiplo):
        self.inicial = inicial
        self.final = final + 1
        self.multiplo = multiplo

    def __iter__(self):
        return self

    def __next__(self):
        while self.inicial < self.final:
          atual = self.inicial
          self.inicial += 1
          if atual % self.multiplo == 0:
            return atual
        raise StopIteration

for n in Multiplos(1,30,3):
    print(n)
#------------------------------------------------------------------------------------------

print('Revisão 6')
def gerar_numeros(n):
    atual = 1
    while atual <= n:
        yield atual
        atual += 1
    

for n in gerar_numeros(5):
    print(n)
#-----------------------------------------------------------------------------------------

print('Revisão 7')
def pares(final):
    inicio = 1
    while inicio < final + 1:
        if inicio % 2 == 0:
            yield inicio
        inicio += 1

for n in pares(10):
    print(n)
#------------------------------------------------------------------------------------------

print('Revisão 8')
def quadrados(lista):
    indice = 0
    while indice < len(lista) - 1:
        atual = lista[indice]
        yield atual ** 2
        indice += 1

for n in quadrados([1, 2, 3, 4, 5]):
    print(n)

#------------------------------------------------------------------------------------------

print('Revisão 9')
def palavra_grande(lista):
    indice = 0
    while indice < len(lista):
        atual = lista[indice]
        if len(atual) >= 5:
            yield atual
        indice += 1

palavras = ["Python","casa","computador","sol","programação"]
for p in palavra_grande(palavras):
    print(p)

#------------------------------------------------------------------------------------------

print('Revisão 10')
def primo(final):
    for num in range(2, final + 1):
        for i in range(2, num):
            if num % i == 0:
                break  # Se achar qualquer divisor, pula para o próximo número
        else:
            yield num  # Só roda se o loop de cima terminar SEM dar break

# Exemplo de uso:
for n in primo(20):
    print(n, end=" ")  # Saída: 2 3 5 7 11 13 17 19


     

        