print('='*5, 'DESAFIO 19', '='*5)

from random import choice
n1 = (input('Insira um nome: '))
n2 = (input('Insira o segundo nome: '))
n3 = (input('insira o terceiro nome: '))
n4 = (input('insira o quarto nome: '))
lista = [n1, n2, n3, n4]
print('O aluno sorteado foi \33[31m{}'.format(choice(lista)))