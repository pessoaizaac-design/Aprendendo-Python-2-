# comprehensions aninhadas
#-----------------------------------------------------------------------------------------
letras = "AB"
numeros = [1, 2, 3]

combinacoes = [f"{letra}{numero}" for letra in letras for numero in numeros]
print(combinacoes)
# ['A1', 'A2', 'A3', 'B1', 'B2', 'B3']
#-----------------------------------------------------------------------------------------
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

achatada = [numero for linha in matriz for numero in linha]
print(achatada)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
#-----------------------------------------------------------------------------------------
tabuada = [[i * j for j in range(1,11)] for i in range(1,11)]
for linha in tabuada:
    print(linha)
#-----------------------------------------------------------------------------------------
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

pares_achatados = [num for linha in matriz for num in linha if num % 2 == 0]
print(pares_achatados)
# [2, 4, 6, 8]
#-----------------------------------------------------------------------------------------

print('Teste 1')
notas = [[7, 8, 5], [9, 10, 6], [4, 3, 8]]
aprovados = [numero for linha in notas for numero in linha if numero >= 6]
print(aprovados)

print('Teste 2')
n = 4
identidade = [[1 if i == j else 0 for j in range(n)]for i in range(n)]

print('Teste 3')
palavras = ['Python', 'Java', 'Sql']
letters = [[letra for letra in palavra] for palavra in palavras]
print(letters)
