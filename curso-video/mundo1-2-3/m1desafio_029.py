'''
Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''

vel = int(input('Velocidade do carro: '))
if vel > 80:
    print('Você está acima da velociadade permitida!\n Velocidade de {} Km/h!'.format(vel))
    multa = 7 * (vel - 80)
    print('Sua multa é de R$ {:.2f}.'.format(multa))
else:
    print('Velocidade dentro do permitido. Boa Viagem') 
print('Nunca deixe de usar o Sinto de Segurança, ele Proteje sua vida!')       