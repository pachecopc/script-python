'''
'''

vel = int(input('Velocidade do carro: '))
if vel > 80:
    print('Você está acima da velociadade permitida!\n Velocidade de {} Km/h!'.format(vel))
    multa = 7 * (vel - 80)
    print('Sua multa é de R$ {:.2f}.'.format(multa))
else:
    print('Velocidade dentro do permitido. Boa Viagem') 
print('Nunca deixe de usar o Sinto de Segurança, ele Proteje sua vida!')       