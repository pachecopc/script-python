'''
'''

dist = int(input('Qual a distância a ser percorrida? '))
if dist <= 200:
    prince = (dist * 0.50)
    print('Preço da passagem: R$ {:.2F}.'.format(prince))
else :
    prince = (dist * 0.45)    
    print('Preço da passagem: R$ {:.2f}.'.format(prince))
    