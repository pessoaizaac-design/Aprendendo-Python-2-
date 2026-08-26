# Revendo python básico completo

print('Exercício 1')
nome = 'Higor'
idade = 18
altura = 1.67
estudando_python = True

print(type(nome))
print(type(idade))
print(type(altura))
print(type(estudando_python))

print('=' * 70)
print('Exercício 2')
a = "10"
b = "5.5"
c = 20

a = int(a)
b = float(b)
print(f'{a} + {b} + {c} = {a + b + c}')

print('=' * 70)
print('Exercício 3')
a = 2
b = 10

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} x {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} ** {b} = {a ** b}')

print('=' * 70)
print('Exercício 4')
salario = 2500
aumento = 1.15

print(f'Uma pessoa recebe {salario} R$ e teve o aumento de 15%, agora ele recebe {salario * aumento}')

print('=' * 70)
print('Exercício 5')
nome = "Higor Pessoa"

print(nome[0])
print(nome[-1])
print(nome[0:5])
print(nome[::-1])
print(len(nome))

print('=' * 70)
print('Exercício 6')
texto = "   Aprender Python é muito bom   "

print(texto.strip())
print(texto.upper().strip())
print(len(texto))
print('Python' in texto)

print('=' * 70)
print('Exercício 7')
user = str(input('Qual é o seu nome: '))
id = int(input('Qual é a sua idade: '))
altura = float(input('Qual é a sua altura: '))

print(f'Seu nome é {user}, você tem {id} anos e {altura}m de altura')

print('=' * 70)
print('Exercício 8')
n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segunfo número: '))

print(f'A média desses números é igual a: {(n1 + n2) / 2}')

print('=' * 70)
print('Exercício 9')
idade2 = 60

if idade2 >=60:
    print('Você é idoso')
elif idade2 >= 18:
    print('Você é maior de idade')
elif idade2 < 18 and idade2 >= 12:
    print('Você é adolescente')
elif idade2 < 12:
    print('Você é uma criança')

print('=' * 70)
print('Exercício 10')
nota = 7.5

if nota < 5:
    print('Aluno reprovado')
elif nota >= 5 and nota <= 6.9:
    print('Aluno em recuperação')
elif nota >= 7:
    print('Aluno aprovado')

print('=' * 70)
print('Exercício 11')
d = 10
e = 20

print(f'{d} > {e}: {d > e}')
print(f'{d} < {e}: {d < e}')
print(f'{d} = {e}: {d == e}')

print('=' * 70)
print('Exercício 12')
f = 35
g = 35

if f > g:
    print(f'{f} é maior que {g}')
elif f < g:
    print(f'{f} é menor que {g}')
elif f == g:
    print(f'{f} é igual a {g}')

print('=' * 70)
print('Exercício 13')
idade3 = 20
salario = 1800

if idade3 >= 18 and salario <= 2000:
    print('Você tem direito ao benefício!')
else:
    print('Você não tem direito ao benefício!')

print('=' * 70)
print('Exercício 14')
é_admin = False
possui_token = True

if é_admin == True or possui_token == True:
    print('Você pode entrar no sistema')
else:
    print('Você não pode entrar no sistema')

print('=' * 70)
print('Exercício 15')

frase = "Python é muito legal"

print('Python' in frase)
print('Java' in frase)
print('legal' in frase)

print('=' * 70)
print('Exercício 16')

palavra = "programacao"
vogais = 'aeiouáéíóúâêîõûãõàèìòù'

palavra = "programacao"
vogais = "aeiouáéíóúâêîõûãõàèìòù"

if set(palavra.lower()) & set(vogais):
    print('Existe uma vogal na palavra')
else:
    print('Não existe vogal na palavra')

print('=' * 70)
print('Exercício 17')
palavra2 = "Python"

print(f'O primeiro caracter dessa palavra é: {palavra2[0]}')
print(f'O último caracter dessa palavra é: {palavra2[-1]}')
print(f'Os três primeiros caracteres dessa palavra são: {palavra2[0:3]}')
print(f'Os quatros últimos caracteres dessa palavra são: {palavra2[2:6]}')
print(f'Essa palavra invertida fica: {palavra2[::-1]}')

print('=' * 70)
print('Exercício 18')
palavra3 = 'Desenvolvimento'

print(f'O primeiro caracter dessa palavra é: {palavra3[0]}')
print(f'O último caracter dessa palavra é: {palavra3[-1]}')
print(f'Essa palavra invertida fica: {palavra3[::-1]}')
print(f'Essa palavra contém: {len(palavra3)} caracteres')

print('=' * 70)
print('Exercício 19')
contador = 1

while contador <= 10:
    print(contador)
    contador += 1


print('=' * 70)
print('Exercício 20')
numbers =[5,10,15,20,0]
cont = 0
indice = 0

while numbers[indice] != 0:
    cont +=numbers[indice]
    indice +=1
print(cont)

print('=' * 70)
print('Exercício 21')
for numero in range(1, 21):
    if numero % 2 == 0:
        continue  
    
    print(numero)

print('=' * 70)
print('Exercício 22')
lista = [10, -5, 20, -2, 15, 0]
som = 0
for n in lista:
    if n < 0:
        continue
    som += n
print(som)

print('=' * 70)
print('Exercício 23')
for v in range(0,101):
    print(v)


print('=' * 70)
for x in range(0,101):
    if x % 2 ==0:
        print(x)

print('=' * 70)
print('Exercício 24')
i = 7
for p in range(1,11):
    print(f'{i} x {p} = {i * p}')

print('=' * 70)
print('Exercício 25')        
numbers2 = [10, 20, 30, 40, 50]

numbers2.append(60)
numbers2.remove(20)
numbers2[2] = 300
numbers2.pop()
print(numbers2)

print('=' * 70)
print('Exercício 26')    
names = ["Ana", "João", "Carlos", "Maria", "Pedro"]
names_pecorrer = iter(names)

while True:
    try:
     print(next(names_pecorrer))
    except StopIteration:
      break

print('=' * 70)
print('Exercício 27') 
tupla = (10, 25, 7, 42, 18)
print(f'O primeiro elemento da tupla é --> {tupla[0]}')
print(f'O último elemento da tupla é --> {tupla[-1]}')
print(f'A quantidade de elemntos da tupla é: {len(tupla)}')
print(f'O maior valor da tupla é: {max(tupla)}')
print(f'O menor valor da tupla é: {min(tupla)}')


print('=' * 70)
print('Exercício 28')
tupla2 = ("Higor", 18, "Python")
nome, idade4, linguagem = tupla2
print(nome)
print(idade4)
print(linguagem)

print('=' * 70)
print('Exercício 29')
nomes = ["Ana", "João", "Carlos", "Maria"]

for indice, elementos in enumerate(nomes):
    print(f'{indice} --> {elementos}')

print('=' * 70)
print('Exercício 30')
produtos = ["Mouse", "Teclado", "Monitor", "Headset", "Webcam"]
for ind, prod in enumerate(produtos):
    print(f'{ind} - {prod}')

print('=' * 70)
print('Exercício 31')
try:
    letras = "abc"
    letras = int(letras)
except ValueError:
    print('Ocorreu um erro...')

print('=' * 70)
print('Exercício 32')
try:
    dividendo = 10
    divisor = 0
    divisao = dividendo / divisor
except ZeroDivisionError:
    print('Você não pode dividir um número por 0')

print('=' * 70)
print('Exercício 33')
id2 = 18
maior_menor = 'Maior de idade' if id2 >=18 else 'Menor de idade'
print(maior_menor)

print('=' * 70)
print('Exercício 34')
par_impar = 17
par_ou_impar = 'Par' if par_impar % 2 == 0 else 'Ímpar'
print(par_ou_impar)

print('=' * 70)
print('Exercício 35')
valor = None
print(valor is None)

print('=' * 70)
print('Exercício 36')
nm = None
if nm is None:
    print('Nenhum nome foi encontrado')
else:
    print(f'{nm}')
