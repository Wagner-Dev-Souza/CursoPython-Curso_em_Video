# Listas utilizam []
# Não são imutaveis como as tuplas, podendo receber novos itens os muda-los, e ainda
# deleta-los
lista = [0, 1, 2, 3, 4] #uma lista com seus índices como elemento
lista[3] = 5 #"valor" do índice 3 modificado para 5
lista.append(5) # adicionado "valor" 5 no índice 5
lista.insert(0, 5) #adicionado "valor" 5 no índice 0
#todos os outros "valores" se reposicionam para o índice seguinte.
del lista[3] #deleta o "valor" alocado no índice 3
lista.pop(3) #deleta o "valor" alocado no índice 3
lista.remove(0) #deleta o primeiro "valor 0" da lista
print(lista)
valores = list(range(4, 11))
print(valores)
baralho = [8, 2, 5, 4, 9, 3, 0]
baralho.sort() #ordena os valores
baralho.sort(reverse=True) #ordena de maneira decrescente
print(baralho)
print(len(baralho)) #mostra o total de índices na lista
if 4 in lista:
    baralho.remove(4)
else:
    print('Não achei o número 4')
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...', end='')
print('\nCheguei ao final da lista.')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

valores = list()
for cont in range(0, 2):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a # faz uma ligação de a com b (qqr alteração afeta as duas)
c = a[:] # faz uma cópia de a em c
b[2] = 8
c[2] = 10
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
