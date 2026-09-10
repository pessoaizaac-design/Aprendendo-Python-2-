print('Desafio 1')
def somar(a,b):
    return a + b
def subtrair(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a, b):
    return a / b
def calcular(a, b, operacao):
    return operacao(a, b)

print(calcular(10,5, multiplicar))
#-----------------------------------------------------------------------------------------

print('Desafio 2')
def dobrar(lista):
    indice = 0
    while indice < len(lista):
        lista[indice] = lista[indice] * 2
        indice += 1
def quadrados(lista):
    indice = 0
    while indice < len(lista):
        lista[indice] = lista[indice] ** 2
        indice += 1
def negativo(lista):
    indice = 0
    while indice < len(lista):
        lista[indice] = lista[indice] * -1
        indice += 1
def operar(lista,funcao):
    funcao(lista)
    print(lista)

numeros = [1, 2, 3, 4, 5]
operar(numeros, dobrar)
#-----------------------------------------------------------------------------------------

print('Desafio 3')
def pares(lista):
    resultado = []
    indice = 0
    while indice < len(lista):
        if lista[indice] % 2 == 0:
            resultado.append(lista[indice])
        indice += 1
    return resultado

def maior_que_dez(lista):
    resultado = []
    indice = 0
    while indice < len(lista):
        if lista[indice] > 10:
            resultado.append(lista[indice])
        indice += 1
    return resultado

def positivos(lista):
    resultado = []
    indice = 0
    while indice < len(lista):
        if lista[indice] > 0:
            resultado.append(lista[indice])
        indice += 1
    return resultado

def filtrar(lista, funcao_filtro):
    dados_filtrados = funcao_filtro(lista)  
    print(dados_filtrados)   

numeros = [-5, 2, 8, 11, -1, 15]

filtrar(numeros, pares)         
filtrar(numeros, maior_que_dez)  
filtrar(numeros, positivos)
#-----------------------------------------------------------------------------------------

print('Desafio 4')
def criar_multiplicador(numero):
    def dobrar():
        return numero * 2
    def triplicar():
        return numero * 3
    return {"Dobro: ", dobrar, 'Triplo: ', triplicar}
#-----------------------------------------------------------------------------------------

print('Desafio 5')
def criar_mensagem(nome):
    def texto(texto):
        return f'{nome}: {texto}'
    return texto

higor = criar_mensagem("Higor")
print(higor("Bom dia!"))
#-----------------------------------------------------------------------------------------

print('Desafio 6')
def criar_contador():
    n = 1
    def aumentar(funcao):
        nonlocal n  
        if funcao():
            n += 1
        return n    
    return aumentar
#-----------------------------------------------------------------------------------------

print('Desafio 7')
def mostrar_execucao(funcao):
    def wrapper(*args, **kwargs):
        print('Executando Função...')
        resultado = funcao(*args, **kwargs)
        print(resultado)
        print('Função Finalizada...\n')
        return resultado
    return wrapper

def somar(a,b):
    return a + b
    
somar = mostrar_execucao(somar)
somar(10,5)
   
#-----------------------------------------------------------------------------------------

print('Desafio 8')
def mostrar_argumentos(funcao):
    def wrapper(*args, **kwargs):
        print(f'ARGUMENTOS: {args or kwargs.items()}')
        resultado = funcao(*args, **kwargs)
        print(f'RESULTADO: {resultado}')
    return wrapper

def soma(a,b):
    return a + b

soma = mostrar_argumentos(soma)
soma(10, 5)
#-----------------------------------------------------------------------------------------

def verificar_positivos(funcao):
    def embrulho(*args, **kwargs):
        for num in args:
            if isinstance(num, (int, float)) and num < 0:
                print(f"Erro: O número {num} é negativo! A função '{funcao.__name__}' não foi executada.")
                return None 
        return funcao(*args, **kwargs)
        
    return embrulho

@verificar_positivos
def somar(a, b):
    return a + b

@verificar_positivos
def calcular_area_retangulo(base, altura):
    return base * altura

print("--- Teste 1: Valores Positivos ---")
resultado1 = somar(10, 5)
print(f"Resultado: {resultado1}\n")

print("--- Teste 2: Um valor Negativo ---")
resultado2 = somar(10, -5)
print(f"Resultado: {resultado2}\n") 

print("--- Teste 3: Área com valor Negativo ---")
resultado3 = calcular_area_retangulo(-4, 5)
print(f"Resultado: {resultado3}\n") #
