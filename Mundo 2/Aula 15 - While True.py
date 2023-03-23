'''while True = executa o camando
dentro do while infinitamente, ou até um break'''

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
# f strings
print(f'A soma vale {s}')
# Utilização das  fstrings a partir do python 3.6
nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.') #fstring modo mais atual e moderno
print('O {} tem {} anos.'.format(nome, idade)) # modo antigo
print('O %s tem %d anos.' % (nome, idade)) # modo arcaico

nome = 'Cláudio'
idade = 35
salário = 987.3
print(f'O {nome:-^20} tem {idade} anos e ganha R$ {salário:.2f}')