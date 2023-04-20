print('\33[31m{:=^30}\33[m'.format(' DESAFIO 89 '))

boletim = list()
nome = list()
nota = list()
while True:
    nome.append(str(input('Nome: ')))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    nome.append(nota[:])
    nota.clear()
    boletim.append(nome[:])
    nome.clear()
    cont = str(input('Quer continuar? [S/N] '))
    if cont in 'nN':
        break

print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for c, i in enumerate(boletim):
    print(f'{c+1:<4}{i[0]:<10}{(i[1][0] + i[1][1])/2:>8.1f}')

while True:
    print('-' * 30)
    aluno = int(input('Mostrar notas de qual aluno? (0 - interrompe) '))
    aluno = aluno - 1
    if aluno == -1:
        print('FINALIZANDO...')
        break
    if aluno <= len(boletim):
        print(f'Notas de {boletim[aluno][0]} são {boletim[aluno][1]}')
print(' <<< VOLTE SEMPRE >>> ')