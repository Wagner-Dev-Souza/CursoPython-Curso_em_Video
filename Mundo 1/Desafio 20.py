print('\33[32m='*5, 'DESAFIO 20', '='*5,'\33[m')

import random
nome1 = input('Digite o nome do aluno 1: ')
nome2 = input('digite o nome do aluno 2: ')
nome3 = input('digite o nome do aluno 3: ')
nome4 = input('digite o nome do aluno 4: ')
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print('A ordem de alunos para apresentação de trabalhos é:\n\33[36m', lista)