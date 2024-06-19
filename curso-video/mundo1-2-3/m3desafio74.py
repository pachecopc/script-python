'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint
numeros = (randint(1, 10) , randint(11, 20), randint(21, 30), randint(31, 40), randint(41, 50))
print('\nOs Números sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior número sorteado é: {max(numeros)}')  
print(f'O menor número sorteado é: {min(numeros)}\n') 


