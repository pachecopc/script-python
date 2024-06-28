'''Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

medida = float(input('\nUma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.1f}cm e {:.1f}mm\n'.format(medida, cm, mm))
