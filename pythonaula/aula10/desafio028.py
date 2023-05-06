# aula 10
from random import randint
escolha = randint(0, 5)
print('xXx' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('xXx' * 20)
n = int(input('Em que número pensei? '))
if n == escolha:
    print('Está correto! Você me venceu!')
else:
    print('Você errou! Eu pensei no {} em vez do {}' .format(escolha, n))








