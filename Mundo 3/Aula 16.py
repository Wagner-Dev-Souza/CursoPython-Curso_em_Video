'''Variáveis compostas'''

'''Tuplas'''
'''tuplas são imutáveis e são escritas com parenteses,
atualmente, os parenteses podem ser ignorados'''

#ex:
lanche = 'Hamburguer' , 'Suco' , 'Pizza' , 'Pudim'
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(len(lanche))

for cont in range(0, len(lanche)):
    print(lanche[cont])
    print(cont)
for comida in lanche:
    print(f'Eu vou comer {comida}')
for pos, comida in enumerate(lanche):
    print(f'Eu comi {comida} na posição {pos}')
print('Comi pra caramba!')
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c)
print(d)
# c != d
print(len(c))#conta o total de itens
print(c.count(5))#conta a qtidade de vezes que o item aparece
print(d.index(4))#mostra a posição em que o item aparece
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)#em python tuplas podem ter itens de tipos diferentes
del(pessoa)#uma tupla pode ser apagada da memoria
