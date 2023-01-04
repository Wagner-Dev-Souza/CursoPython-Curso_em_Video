print('='*5, 'DESAFIO 33', '='*5)

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print('O maior número neste caso é {}'.format(maior))
menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c
print('O menor número neste caso é {}'.format(menor))


