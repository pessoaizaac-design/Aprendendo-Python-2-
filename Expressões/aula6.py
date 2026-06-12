#Meta caracteres $ ^

import re

cpf = '101.782.124-07'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.findall(r'[^0-9]+', cpf))