print('\33[31m{:=^30}\33[m'.format(' DESAFIO 84 '))

pessoas = list()
dados = list()

while True:
    dados.append(str(input('nome: ')))
    dados.append(float(input('peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    cont = str(input('Quer continuar S/N? '))
    if cont in 'nN':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
pesomai = pesomen = 0
nomemai = list()
nomemen = list()
for p in pessoas:
    if pesomen == 0:
        pesomen = p[1]
        pesomai = p[1]
    elif p[1] < pesomen:
        pesomen = p[1]
    elif p[1] > pesomai:
        pesomai = p[1]
for n in pessoas:
    if n[1] == pesomai:
        nomemai.append(n[0])
    elif n[1] == pesomen:
        nomemen.append(n[0])
print(f'O maior peso foi de {pesomai}Kg. Peso de {nomemai}')
print(f'O menor peso foi de {pesomen}Kg. Peso de {nomemen}')