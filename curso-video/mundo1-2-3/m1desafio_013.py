'''Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

salário =float(input('Qual o valor do salário? R$ '))
novo = salário + (salário * 15 / 100)
print('O salário atual é R$ {:.2f}, como o aumento de 15% passa a ser de R$ {:.2f}'.format(salário, novo))
