nome1 = list()
nome1.append("Pedro")
nome1.append(25)
nome2 = list()
nome2.append("Maria")
nome2.append(19)
nome3 = list()
nome3.append("João")
nome3.append(32)

#Listas compostas
pessoas = list()
pessoas.append(nome1[:])
pessoas.append(nome2[:])
pessoas.append(nome3[:])
print(pessoas)
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])

galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen +=1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')