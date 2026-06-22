# len --> ler a quantidade de elementos
# in | not in

# | = União
# & = Aparecem nos dois
# - = Diferença de um
# ^ = Diferença dos dois
# isdisjoint() = elemenos em comum
# copy() = copiar
# add() = Adicionar item
# remove() = Remover item
# discard() = Remover e não mostar o erro
# pop = Remover aleatoriamente
# clear() = Remover tudo




#planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
#print(planeta_anao)

#qtde_p = len(planeta_anao)
#print(qtde_p)

#for astro in planeta_anao:
    #print(astro.upper())
    
#astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
#print('Lista:', astros)
#astroSet = set(astros)
#print('Conjuto:', astroSet)


try:
    p1 = {'Terra', 'Vênus', 'Mercúrio', 'Marte', 'Netuno'}
    p2 = {'Terra', 'Júpiter', 'Urano', 'Marte', 'Saturno'}
    p3 = {'Júpiter', 'Urano', 'Saturno'}
    print(p1 | p2)
    print('=' * 65)
    print(p1 & p2)
    print('=' * 65)
    print(p1 - p2)
    print('=' * 65)
    print(p1 ^ p2)
    print('=' * 65)
    print(p1.isdisjoint(p3))
    print('=' * 65)
    p4 = p1.copy()
    print('P1:', p1)
    print('P4:', p4)
    print('=' * 65)
    p1.add('Júpiter')
    print(p1)
    print('=' * 65)
    p1.remove('Terra')
    print(p1)
    print('=' * 65)
    p1.discard('Terra')
    print(p1)
except Exception as erro:
    print(f'Ocorreu um erro inesperado: {erro}')


