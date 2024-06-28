''' Faça u  programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e toodas
as informaçoes possíveis sobre ela.
'''
a = input('Digite algo:')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços ?', a.isspace())
print('É um número ?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumerico?', a.isalnum())
