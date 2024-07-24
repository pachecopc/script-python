'''Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

dist = int(input('Qual a distância a ser percorrida? '))
if dist <= 200:
    prince = (dist * 0.50)
    print('Preço da passagem: R$ {:.2F}.'.format(prince))
else :
    prince = (dist * 0.45)    
    print('Preço da passagem: R$ {:.2f}.'.format(prince))
    