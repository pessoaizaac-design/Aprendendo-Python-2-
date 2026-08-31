# Revendo python intermédiario completo

# Def
print('Exercício 1')
def saudacao(nome):
    print(f'Olá, {nome}! Seja bem-vindo ao Python')

saudacao('Higor')
print('=' * 70)

print('Exercício 2')
def calcular_dobro(numero):
    print(f'{numero} x 2 = {numero*2}')

calcular_dobro(15)
print('=' * 70)

# Args / Kwargs
print('Exercício 3 e 4')
def apresentar(**kwargs):   
    print(f'Meu nome é {kwargs['nome']}, tenho {kwargs['idade']} e moro em {kwargs['cidade']}')

apresentar(cidade = "Recife", idade = 18, nome = "Higor")
print('=' * 70)

# Valores padrões + None
print('Exercício 5')
def boas_vindas(nome='Visitante'):
    print(f'Olá {nome}')

boas_vindas('Higor')
#boas_vindas()
print('=' * 70)

print("Exercício 6")
def mostrar_idade(idade=None):
    if idade == None:
        print('Idade não informada.')
    else:
        print(f'Você tem {idade} anos')
mostrar_idade(18)
print('=' * 70)

# Escopo + Global
print("Exercício 7")
nome = 'Higor'
def linguagem():
    print(nome)

linguagem()
print('=' * 70)

print('Exercício 8')
contador = 0
def incrementar():
    global contador
    contador += 1
    print(contador)

incrementar()
incrementar()
incrementar()
print('=' * 70)

# Return
print('Exercício 9')
def somar(numero1, numero2):
    return f'{numero1} + {numero2} = {numero1 + numero2}'

resultado = somar(10,20)
print(resultado)
print('=' * 70)

print('Exercício 10')
def calcular_media(nota1, nota2, nota3):
    return f'A média dessas notas é igual a: {(nota1+nota2+nota3) / 3:.2f}'

minha_media = calcular_media(7.5, 8.0, 9.0)
print(minha_media)
print('=' * 70)

# Args
print('Exercício 11')
def somar_tudo(*args):
    print(f'A soma de todos os números é igual a: {sum(args)}')
somar_tudo(10, 20, 30, 40)
print('=' * 70)

print('Exercício 12')
def maior_numero(*args):
    resultado = max(args)
    print(f'O maior número entre eles é: {resultado}')
maior_numero(10, 45, 7, 89, 23)
print('=' * 70)

# Higher Order Functions / First-Class Functions
print('Exercício 13')
def dobrar(n):
    print(f'Esse número x 2 é igual a: {n  * 2}')
def executar(funcao, valor):
    funcao(valor)
executar(dobrar,10)
print('=' * 70)

print('Exercício 14')
def somar(a,b):
    print(f'A soma desses números é igual a: {a + b}')
def multiplicar(a,b):
    print(f'A multiplicação desses números é: {a * b}')
def calcular(funcao, v1, v2):
    funcao(v1,v2)
calcular(somar,10,5)
calcular(multiplicar,10,5)
print('=' * 70)

# Closure
print('Exercício 15')
def criar_saudacao(name):
    def saudar():
     return f'Olá, {name}!'
    return saudar
saudacao_higor = criar_saudacao("Higor")
print(saudacao_higor())
print('=' * 70)

print('Exercício 16')
def criar_multiplicador(number):
    def dobrar(number2):
        return f'{number2 * number}'
    return dobrar
dobrar = criar_multiplicador(2)
print(dobrar(10))
print('=' * 70)

# Dict
print('Exercício 17')
instrumentos = {'nome': 'Higor', 'idade': 18,'linguagem': 'Python'}
print(instrumentos['nome'])
print(instrumentos['idade'])
print(instrumentos['linguagem'])
print('=' * 70)

print('Exercício 18')
produtos = {
    'nome': 'mouse',
    'preco': 80,
    'estoque': 15
}
produtos['preco'] = 95
produtos['marca'] = 'Logitech'
produtos['estoque'] = 14
print(produtos)
print('=' * 70)

# Métodos de dict
print('Exercício 19')
usuario = {
    "nome": "Higor",
    "idade": 18,
    "cidade": "Recife"
}

for chave,valor in usuario.items():
    print(f'{chave}')
    print(f'{valor}')
    print(f'{chave}: {valor}')
    print('-' * 20)
print('=' * 70)

print('Exercício 20')
config = {
    "tema": "escuro",
    "idioma": "pt-BR",
    "notificacoes": True
}
print(config.get('tema'))
print(config.get('fonte', 'não informada'))
print(config.pop('idioma'))
