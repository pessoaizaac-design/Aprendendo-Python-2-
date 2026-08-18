
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



# Args e Kwargs

# *args --> permite você pasar quantos valores de posição você quiser

def calcular_imposto(valor, *pecr_ir):
    total_imposto = 0
    for v in pecr_ir:
        total_imposto += valor * v
    return total_imposto


print(calcular_imposto(1000, 0.275, 0.05, 0.0375, 0.03))

# **kwargs é o args, porém você deve nomear os parâmetros!
# kwargs.value() --> para você acessar os valores dados para os parâmetros

def cll_imps(valor, **kwargs):
    total_imposto = 0
    for v in kwargs.values():
        total_imposto += valor * v
    return total_imposto

print(cll_imps(1000, perc_ir=0.275, perc_iss=0.05, perc_csll=0.0375, perc_pis=0.03))





