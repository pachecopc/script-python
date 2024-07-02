'''Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''

larg = float(input('Largura da Parede '))
alt = float(input('Altura da Parede '))
área = larg * alt
print('Sua parde tem dimensão de {}x{} e a sua área é de {}m.'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisara de {}l de tinta.'.format(tinta))

