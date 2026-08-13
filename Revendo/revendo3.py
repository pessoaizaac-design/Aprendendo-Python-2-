import re

texto = "Meu CPF é 12345678900 e meu telefone é 81987654321."

print(re.findall(r'[0-9]+', texto, flags=re.I))

texto2 = "Python é uma linguagem incrível. Eu estudo Python todos os dias."

print(re.findall(r'Python', texto2, flags=re.I))

emails = '''
higor@gmail.com
teste@hotmail.com
abc123@outlook.com

higor@gmail
@gmail.com
higor.com
'''

print(re.findall(r'^\w+\@\w+\.com$', emails, flags=re.M|re.I))

number =  "Meu telefone é 81987654321."

print(re.sub(r'\d+', '[TELEFONE]',number))


texto = """
Nome: Higor
Idade: 18
Email: higor@gmail.com
Telefone: 81987654321
"""

resultado = re.search(
    r'Nome:\s*(\w+)\s*Idade:\s*(\d+)\s*Email:\s*(\S+)\s*Telefone:\s*(\d+)',
    texto
)

print(resultado.groups())