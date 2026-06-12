import re

string = 'Este é um teste de expressões teste regulares'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'ABC', string, count = 1))

regexp = re.compile('teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string))