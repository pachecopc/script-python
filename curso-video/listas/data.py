from datetime import datetime
nasc = int(input('Em que ano você nasceu? \n'))
ano_atual = datetime.now().year

idade = (ano_atual - nasc)
if idade < 18 :
    print('Você tem {} anos em {} e vai se alisar daqui a {} anos, em {}.'.format(idade, ano_atual, (18 - idade), (nasc + 18)))
elif idade > 18 :
    print('Você tem {} anos e ja passou seu período de alintamento.'.format(idade)) 
else:
    print('Voce te {} anos. Esta na hora de se alistar.'.format(idade))       

