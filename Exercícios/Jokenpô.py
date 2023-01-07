from random import choice

print('-=-' * 10)
print('\33[31m          JOKENPÔ\33[m')
print('-=-' * 10)
lista = ['0', '2', '5']
x = choice(lista)
print('\33[33m5 - \33[34mPapel\n'
      '\33[33m0 - \33[34mPedra\n'
      '\33[33m2 - \33[34mTesoura\33[m')
n = input('Faça sua escolha: ')
print('\33[36mEu escolhi',x)
if n == '5' and x == '0':
    print('\33[32mVocê me venceu: papel embrulha pedra!!!')
elif n == '5' and x == '2':
    print('\33[31mVocê perdeu: tesoura corta papel!!!')
elif n == '2' and x == '0':
    print('\33[31mVocê perdeu: pedra quebra tesoura!!!')
elif n == '2' and x == '5':
    print('\33[32mVocê me venceu: tesoura corta papel!!!')
elif n == '0' and x == '5':
    print('\33[31mVocê perdeu: papel embrulha pedra!!!')
elif n == '0' and x == '2':
    print('\33[32mVocê me venceu: pedra quebra tesoura!!!')
else:
    print('\33[33mFalhou... Tente outra vez!!!')
