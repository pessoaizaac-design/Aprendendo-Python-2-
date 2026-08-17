import sys
import time

try: 
# Ainda não é um gerador
 def gera():
   variavel = 'Valor 1'
   yield variavel # Tranforma em um gerador, navegação lenta!
   variavel = 'Valor 2'
   yield variavel 
   variavel = 'Valor 3'
   yield variavel
except Exception as e:
  print(f'Ocorreu um erro: {e}') 

#pg = gera()

l1 = [x for x in range(1000)]
#print(type(l1)) --> Retorna o temo '__list__'
l2 = (x for x in range(1000))
#print(type(l2)) --> Retorna o termo "__generator__"

print(sys.getsizeof(l1))
print(sys.getsizeof(l2)) # Um gerador consome menos memória e controlamos o que desejamos dele

# Exercitando

def pares(n):
  for n in range(n + 1):
    if n % 2 == 0:
     yield n

for numeros in pares(10):
  print(numeros)
  





