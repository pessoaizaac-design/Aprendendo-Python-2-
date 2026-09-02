# Revendo python intermédiario 3

# generator function
print('Exercício 51')
def numeros():
    for n in range(1,6): 
        yield n
    
for x in numeros():
    print(x)

#---------------------------------------------------------------------------

print('Exercício 52')
def contagem_regressiva():
    funcoes = []
    for n in range(5, 0, -1):
        def wrapper(value=n):
            yield value
        funcoes.append(wrapper)        
    return funcoes
listar_funcoes = contagem_regressiva()
for f in listar_funcoes:
    print(next(f()))

#---------------------------------------------------------------------------

# yield from
print('Exercício 53')
def contagem():
    lista = [1, 2, 3]
    yield from lista
for valor in contagem():
    print(valor)

#---------------------------------------------------------------------------

print('Exercício 54')
def mudar_contagem():
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    if valor in lista1:
        yield from lista1 
    yield from lista2
for value in mudar_contagem():
    print(value)

#---------------------------------------------------------------------------

# Exceptions
print('Exercício 55')
def divisao(n1,n2):
    try:
        print(f'{n1} / {n2} = {n1/n2}')
    except ValueError and ZeroDivisionError as e:
        print(f'Houve um erro: {e}')
divisao(10,2)
divisao(10,0)

#---------------------------------------------------------------------------

print('Exercício 56')
def obter_elemento(lista, indice):
 try:
    elemento = lista[indice]
    print(f"Elemento do índice {indice}: {elemento}")
    return elemento
 except IndexError as a:
     print(f'ERRO: {a}')
 except TypeError as b:
     print(f'ERRO: {b}')
my_list = ['Higor', 'Python', 'Java']

# caso 1
obter_elemento(my_list, 1)
# caso 2
obter_elemento(my_list, 10)
# caso 3
obter_elemento(my_list, 'A')

#---------------------------------------------------------------------------

# else and finally
print('Exercício 57')
def division(n1, n2):
    try:
        n1 / n2
    except Exception:
        print('Não foi possível realizar a divisão.')
    else:
        print('Divisão realizado com sucesso!')
# caso 1
division(10,0)
# caso 2
division(10,5)

#---------------------------------------------------------------------------

print('Exercício 58')
valor2 = '123'
try:
    valo2 = int(valor2)
finally:
    print('Programa realizado')

#---------------------------------------------------------------------------

# raise
print('Exercício 59')
def verificar_idade(idade):
    if idade < 0:
        raise ValueError('Idade não pode ser negativa')
    return idade
id = verificar_idade(18)
print(id)

#---------------------------------------------------------------------------

print('Exercício 60')
def sacar(saldo, valor):
    if valor > saldo:
         raise ValueError('Saldo insuficiete')
    return "Saque efetuado com sucesso"
money = sacar(400, 300)
print(money)

#---------------------------------------------------------------------------

