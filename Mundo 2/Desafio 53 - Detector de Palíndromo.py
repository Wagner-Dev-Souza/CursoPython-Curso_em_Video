print('\33[33m{:=^30}\33[m'.format(' DESAFIO 53 '))

'''palavra = str(input('Digite uma frase: ')).lower().strip().replace(' ', '')
if palavra == palavra[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo') -> forma sem itilizar for'''

# forma com for

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')