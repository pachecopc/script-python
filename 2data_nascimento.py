from datetime import date
nome = input ('Qual é o seu nome?') 
print('='*20)
dia = input ('Em que dia você nasceu?') 
print('='*20)
mes = input ('Em que mês você nasceu?')
print('='*20)
ano1 = int(input ('Em que ano você nasceu?'))
print('='*20)

ano = date.today().year
print(nome,'nasceu em?',dia,'de', mes,'de', ano1)

subtracao = ano - ano1
print(nome, 'tem',subtracao, 'anos de idade.')