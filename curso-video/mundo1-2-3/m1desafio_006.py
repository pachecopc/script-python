'''Crie um algoritimo que leia um número e mostre seu dobro, triplo e raiz quadrada.'''

n = int(input('Digite um número:'))
print('O Dobro de {} vale {}'.format(n, (n*2)))
print('O Triplo de {} vale {}. \nA Raiz Quadrada de {} é {:.2f}' .format(n, (n*3), n, (n**(1/2))))
