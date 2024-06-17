'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética.d) Em que posição está o time da Cruzeiro.
'''

times = ('Botafogo','Flamengo', 'Bahia', 'Athletico-PR', 'São Paulo', 'Bragantino', 'Palmeiras', 'Cruzeiro',
        'Atlético-MG', 'Internacional','Juventude', 'Fortaleza', 'Atlético-GO', 'Cuiabá', 'Vasco',
         'Corinthians', 'Grêmio', 'Criciúma', 'Fluminense', 'Vitória')
print('-='*25)
print(f'\nLista de Times do Brasileirão 2024: {times}')
print('-='*25)
print(f'\nOs 5 priemiros colocados são: {times[0:5]} \n')
print('-='*25)
print(f'\nOs últimos 4 times são: {times[-4:]}\n')
print('-='*25)
print(f'\nTimes em oredem Alfabética: {sorted(times)}\n ')
print('-='*25)
print(f'\nO Cruzeiro está em {times.index("Cruzeiro")+1}ª posição\n')
