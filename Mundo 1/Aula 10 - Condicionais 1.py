carro = ('obj')
bloco = ('Comandos para o carro')

#carro.siga()
#se carro.esquerda()
#    bloco_Verdadeiro_
#senão
#    bloco_Falso_

#if carro.esquerda():
#    bloco True
#else:
#   bloco False
#carro.pare()

#exemplo:
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
#escrita simplificada no python:
print('Carro novo' if tempo<=3 else 'Carro velho')
print('--FIM--')

nome = str(input('Qual é o seu nome? ')).strip()
if nome.upper() == 'WAGNER':
    print('Que nome lindo você tem!')
print('Bom dia {}!'.format(nome))
print('--FIM--')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >= 6:
    print('PARABÉNS!!!')
else:
    print('Estude Mais...')
print('--FIM--')
