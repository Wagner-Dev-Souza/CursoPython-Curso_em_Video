print('='*5, 'DESAFIO 26', '='*5)

F = input('Digite uma frase: ').strip()

c = F.lower().count('a')
a1 = F.lower().find("a")+1
a2 = F.lower().rfind('a')+1

print('A letra "a" aparece um total de \33[31m{}\33[m vezes. '.format(c))
if c > 1:
    print('Primeiro na posição \33[32m{}\33[m e por último na posição \33[32m{}\33[m'.format(a1, a2))
if c == 1:
    print('Apenas na posição \33[35m{}\33[m'.format(a1))
else:
    print('')
