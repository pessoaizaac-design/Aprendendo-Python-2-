import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div> 
'''

print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', texto))
print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', texto))
