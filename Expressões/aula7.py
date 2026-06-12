# \w ==> [a-zA-Z0-9À-ù]
# \w ==> [a-zA-Z0-9]  ==> flags=re.A

# \W ==> [^a-zA-Z0-9À-ù_]
# \W ==> [^a-zA-Z0-9_] ==> flags=re.A

# \d ==> [0-9]
# \D ==> [^0-9]

# \s ==> [\r\n\f\t]
# \S ==> [a-zA-Z0-9À-ù_]

# \b ==> r'\be\w+' = começam com e
# r'\w+e\b' = terminam com e


import re

texto = '''
João trouxe   flores para a sua amada namorada em 10 de janeiro de 1970.
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente. maria, hoje sua esposa, ainfa faz aquele café com pão de queijo nas tardes de domingo. Tambem né! Sendo a boa mineira que é, nunca esquece seu famoso pão de queijo.
Não canso de ouvir Maria:
"Joooooooooãooooooo, o café tá prontinho aqui! veemmm."
'''

#print(re.findall(r'[a-z]{1,}', texto, flags=re.I))
#print(re.findall(r'[a-zA-Z]{1,}', texto))

#print(re.findall(r'[a-zA-Z0-9]{1,}', texto))
#print(re.findall(r'[a-zA-Z0-9À-ù]{1,}', texto))

#print(re.findall(r'\w+', texto,flags=re.I))
#print(re.findall(r'\W+', texto,flags=re.I))

#print(re.findall(r'\d+', texto,flags=re.I))
#print(re.findall(r'\D+', texto,flags=re.I))

#print(re.findall(r'\s+', texto,flags=re.I))
#print(re.findall(r'\S+', texto,flags=re.I))

#print(re.findall(r'\be\w+', texto, flags=re.I))
#rint(re.findall(r'\w+e\b', texto, flags=re.I))