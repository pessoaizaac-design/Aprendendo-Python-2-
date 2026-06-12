import re

texto = '''
João trouxe   flores ára a sua amada namorada em 10 de janeiro de 1970.
Maria era o nome dela.


Foi um ano excelente na vida de João. Teve 5 filhos, todos adultos atualmente. maria, hoje sua esposa, ainfa faz aquele café com pão de queijo nas tardes de domingo. Tambem né! Sendo a boa mineira que é, nunca esquece seu famoso pão de queijo.
joão não canso de ouvir maria:
"Joooooooooãooooooo, o café tá prontinho aqui! veemmm."
'''

print(re.search(r'João', texto))

print('=' *50)

print(re.findall(r'João', texto))

print('=' *50)

regexp = re.compile('João')
print(regexp.search(texto))
print(regexp.findall(texto))

print('=' * 50)

print(re.findall(r'João|Maria|to..s', texto))
print(re.findall(r'[Jj]oão|[Mm]aria', texto))
print(re.findall(r'JOão|MArIa', texto, flags=re.I))

print('=' * 50)

print(re.findall(r'Jo*ão*', texto))

print('=' * 50)

print(re.findall(r'Jo+ão+', texto))

print('=' * 50)

print(re.findall(r'Jo{1,}ão{1,}', texto))

print('=' * 50)

texto2 = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div> 
'''

print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', texto2))

