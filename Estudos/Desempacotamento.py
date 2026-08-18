# Desempacotamento de iteráveis (*args)

full_name = ('Higor', 'Izaac', 'Pessoa')
firstname, lastname, *rest = full_name

#print(firstname, lastname, *rest) # --> Rest mostra tudo que sobrou da sus Lista ou Tupla.

#print(*full_name) # ==> firstname, lastname = full_name

a,b = 1,2
a,b = b,a
#print(a, b)

def the_args(*args):
    first, second = args
    print(args)
    print(first, second)

the_args('One', 'Two')

list_multi = [[1,2], [3,4]]
[one,two], [three, four] = list_multi
print(one, two, three, four)

lista = [*range(1,11)] # Desempacato o range e empacota ele em uma lista
print(lista)