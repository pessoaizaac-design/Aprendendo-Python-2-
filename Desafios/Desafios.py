from functools import reduce

# Map, Filter and Reduce

valores = [10, 25, 50, 100, 200]

novos_valores = list(map(lambda p: p * 0.90, valores))
print(novos_valores)

idades = [12, 17, 18, 21, 15, 30, 16, 25]

maiores = list(filter(lambda id: id >= 18, idades))
print(maiores)

numeros = [5, 10, 15, 20]

total = reduce(lambda soma, valores: soma + valores, numeros, 0 )
print(total)