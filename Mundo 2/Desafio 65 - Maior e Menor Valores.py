print('\33[33m{:=^30}\33[m'.format(' DESAFIO 65 '))

resposta = 'S'
soma = 0
cont = 0
maior = 0
menor = 0
while resposta == 'S':
    n = int(input('Digite um número inteiro: '))
    resposta = str(input('Deseja continuar digitando (S/N)? ').upper())
    soma += n
    cont += 1
    media = soma / cont
    if maior == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('\nVocê digitou {} números,\n'
      'a soma entre eles é {} e a média é igual a {:.2f}\n'
      'o maior número foi {} e o menor {}'.format(cont, soma, media, maior, menor))