# Desafio 1

for n in range(0,101):
    if n % 2 == 0:
        print(n)

print('=' * 50)

# Desafio 2

cont = 0
while True:
    n = int(input('Digite um número: '))
    if n >= 1:
        cont +=1
    else:
        break
print(f'Você digitou {cont} números positivos')


print('=' * 50)

# Desafio 3

numbers = []

for n in range(1,11):
    n = int(input('Diga um valor para a lista: '))
    numbers.append(n)

print('=' * 50)

print(f'O maior número indicado foi: {max(numbers)}')
print(f'Já o menor valor indicado foi: {min(numbers)}')
print(f'A soma total dos seus valores é igual a = {sum(numbers)}')
print(f'E a média dos seus números é igual a = {sum(numbers)/ len(numbers)}')

print('=' * 50)

# Desafio 4 

con = 0

text = str(input('Digite uma frase: '))
text = text.lower()

print('=' * 50)

for letra in text:
    if letra in "aeiouáéíóúâêîôûãõ":
        con +=1
print(f'A frase digitada contém {con} vogais!')

print('=' * 50)

# Desafio 5 

c = 0 
b = 0

for aluno in range(5):
    nome = input('Nome: ')
    nota = float(input('Nota: '))

    # IMPORTANTE: Todo este bloco agora está alinhado (indentado) dentro do for
    if nota >= 7:  # Corrigido de 'n' para 'nota'
        c += 1
        print(f'''Aluno: {nome}
Nota: {nota}
Situação: Aprovado\n''')
    else: 
        b += 1
        print(f'''Aluno: {nome}
Nota: {nota}
Situação: Reprovado\n''')

# Mostra o resultado final depois que o laço terminar
print(f'Total de aprovados: {c}')
print(f'Total de reprovados: {b}')



