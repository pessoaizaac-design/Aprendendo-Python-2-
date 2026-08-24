# Args

print('Desafio 1 Args')
def calcular_media(*args):
    total_soma = sum(args)
    numeros_contagem = len(args)

    media = total_soma / numeros_contagem

    return f'A média dos números informados é igual a: {media}'
print(calcular_media(10, 20, 30, 40))

print('=' * 70)

print('Desafio 2 Args')
def maior_e_menor(*args):
    maior = args[0]
    menor = args[0]

    for numero in args:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero
    return maior, menor

print('=' * 70)

# Kwargs
print('Desafio 1 Kwargs')
def exibir_usuario(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')    

exibir_usuario(
    Nome="Higor",
    Idade=18,
    Curso="Ciência da Computação"
)

print('=' * 70)
print('Desafio 2 kwargs')
def filtrar_dados(**kwargs):
    for chave, valor in kwargs.items():
        if isinstance (valor, str):
            print(f'{chave}: {valor}')

filtrar_dados(
    nome="Higor",
    idade=18,
    curso="CC",
    cidade="Recife",
    ativo=True
)