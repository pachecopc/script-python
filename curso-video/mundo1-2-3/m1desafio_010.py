'''Exercício Python 010: Crie um programa que leia quanto
 dinheiro uma pessoa tem na carteira e 
 mostre quantos dólares ela pode comprar.
'''
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.51
print('Com R$ {:.2f} você pode comprar Us$ {:.2f}'.format(real, dolar))
