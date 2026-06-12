# Meta Caracteres : ^ $ ()
# * 0 ou n
# +  1 ou n
# ?  0 ou 1
# {n / min / max}  


import re

texto = '''
João trouxe   flores ára a sua amada namorada em 10 de janeiro de 1970.
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente. maria, hoje sua esposa, ainfa faz aquele café com pão de queijo nas tardes de domingo. Tambem né! Sendo a boa mineira que é, nunca esquece seu famoso pão de queijo.
Não canso de ouvir Maria:
"Joooooooooãooooooo, o café tá prontinho aqui! veemmm."
'''

print(re.findall(r'jo+ão+', texto, flags = re.I))
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))

texto2 = 'João ama ser amado'
print(re.findall(r'ama[do]*', texto2, flags=re.I))