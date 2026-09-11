print("Desafio 1")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7 ,8, 9]
]

matriz_unica = [numero for linha in matriz for numero in linha]
print(matriz_unica)

#-----------------------------------------------------------------------------------------

print("Desafio 2")
matriz_2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

matriz_pares = [numero for linha in matriz_2 for numero in linha if numero % 2 == 0]
print(matriz_pares)

#-----------------------------------------------------------------------------------------

print("Desafio 3")
numeros = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

numeros_elevados = [num ** 2 for linha in numeros for num in linha]
print(numeros_elevados)

#-----------------------------------------------------------------------------------------

print("Desafio 4")
palavras = [
    ["python", "java", "c"],
    ["html", "css", "javascript"],
    ["ruby", "go", "rust"]
]

maior_que_tres = [elemento for linha in palavras for elemento in linha if len(elemento) > 3]
print(maior_que_tres)

#-----------------------------------------------------------------------------------------

print("Desafio 5")
tabela = ([[i * j for j in range(1,6)] for i in range(1,6)])
print(tabela)
