from random import randint
from time import sleep

print('=--' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...'.upper())
print('=--' * 20)
pc = randint(0, 5)                                     #computador pensa.
jogador = int(input('Em que número eu pensei? '))      #jogador tenta adivinhar.
print('PROCESSANDO...')
sleep(0.7)
print('Você acertou! Parabéns!'if pc == jogador else f'Você errou! Eu pensei no número {pc} e não no {jogador}')
