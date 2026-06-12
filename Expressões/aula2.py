# Meta Caracteres : . ^ $ * + ? { } [ ] \ | ( )
# | = OU
# . = Qualquer Caracter
# [] = Conjuto de caracteres

import re

texto = '''
João trouxe   flores ára a sua amada namorada em 10 de janeiro de 1970.
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente. maria, hoje sua esposa, ainfa faz aquele café com pão de queijo nas tardes de domingo. Tambem né! Sendo a boa mineira que é, nunca esquece seu famoso pão de queijo.
Não canso de ouvir Maria:
"Joooooooooãooooooo, o café tá prontinho aqui! veemmm."
'''

print(re.findall(r'João|Maria|ad..tos', texto))
print('=' * 20)
print(re.findall(r'[Jj]oão|[Mm]aria', texto))
print(re.findall(r'JOÃO|MaRia', texto, flags=re.IGNORECASE))