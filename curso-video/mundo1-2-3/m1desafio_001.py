#crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas vindas de acordo com o valor digitado, e a 1º letra sera  maiuscula.

entrada = input('Digite seu nome: \n')
print('Olá',entrada.title(),'prazer te conhecer!'.format(entrada))
print('<<<<<<--- Volte sempre ---->>>>>>\n')