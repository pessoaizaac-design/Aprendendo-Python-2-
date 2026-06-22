import re

string = 'Este é um teste de expressões teste regulares'

#print(re.search('teste', string))
#print(re.findall('teste', string))
#print(re.sub('teste', 'ABC', string))

regexp = re.compile('teste')

#print(regexp.findall(string))
#print(regexp.search(string))
#print(regexp.sub('ABC', string))

texto = '''
João trouxe   flores ára a sua amada namorada em 10 de janeiro de 1970.
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente. maria, hoje sua esposa, ainfa faz aquele café com pão de queijo nas tardes de domingo. Tambem né! Sendo a boa mineira que é, nunca esquece seu famoso pão de queijo.
Não canso de ouvir Maria:
"Joooooooooãooooooo, o café tá prontinho aqui! veemmm."
'''

texto2 = 'João ama ser amado'

#print(re.findall(r"joão|maria|ad..tos", texto))
#print(re.findall(r'[jJ]oão|[mM]aria', texto))
#print(re.findall(r'JOão|MARia', texto, flags=re.I))

#print(re.findall(r'jo+ão', texto, flags=re.I))
#print(re.findall(r'jo{1,}ão', texto, flags=re.I))
#print(re.findall(r'ama[do]*', texto2, flags=re.I))

texto3 = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div> 
'''

#print(re.findall(r'<[divp]{1,3}>.*?<\/[divp>]{1,3}',texto3, flags=re.IGNORECASE))

cpf = '101.782.124-07'

#print(re.findall(r'((?:[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}))', cpf))
#print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
#print(re.findall(r'[^0-9]+', cpf))










