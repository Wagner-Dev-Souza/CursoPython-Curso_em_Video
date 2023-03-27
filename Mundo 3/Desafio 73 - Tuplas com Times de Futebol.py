print('\33[31m{:=^30}\33[m'.format(' DESAFIO 73 '))

times = 'Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba','Cuiabá', 'Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude'
print('-='*20)
print(f'Lista de times do Brasileirão 2022: {times}')
print('-='*20)
print(f'Os 5 primeiros times são {times[0:5]}')
print('-='*20)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*20)
print(f'Times em ordem alfabética: {sorted (times)}')
print('-='*20)
print('O Botafogo esta na {}ª posição'.format(times.index('Botafogo') + 1))
print('-='*20)