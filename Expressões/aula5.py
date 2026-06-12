# Meta Caracteres : ()

import re
#from pprint import pprint

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>Massa</div> 
'''

cpf = '101.782.124-07'
print(re.findall(r'((?:[0-9]{3})\.[0-9]{3}\.[0-9]{3}-[0-9]{2})', cpf))

#tags = re.findall(r'<([dpiv]{1,3})>(?:.+?)<\/\1>', texto)
#pprint(tags)

#for tag in tags:
#    um,dois,tres = tag
#    print(dois,tres)