
import time

# criar um decorator para calcular tempo
def calcular_tempo(funcao):
    def wrapper(n1, n2):
        tempo_inicial = time.time()
        funcao(n1, n2)
        tempo_final = time.time()
        print(f'A duração foi de {tempo_final - tempo_inicial} segundos')
    return wrapper

@calcular_tempo
def calcular_potencia(n1, n2):
    print(f'{n1} elevado a {n2} é igual a: {n1**n2}')
    return n1 ** n2

calcular_potencia(2,2)



