nome  = input('Digite o seu nome: ')
capitalized_nome = nome.capitalize()
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a altura: '))
if altura >2.49 :
   imc = (altura**2 - altura**2)
   print('Altura Incorreta')
   altura = float(input('Digite a altura correta: '))
if altura < 2.48:
   imc = peso /(altura**2)
   print('---------------------------------------------')
   print(f'{nome.capitalize()},seu IMC é: {imc:.2f}\n')
   if imc < 18.5:
       print('Você esta Abaixo do Peso\n ')
   elif 18.5 <= imc < 25:
        print('Parabéns , você esta no peso Ideal\n')
   elif 25 <= imc < 30:
        print('Você esta com sobrepeso, Cuidado!\n ')
   elif 30 <= imc < 40:
        print('Você esta com Obesidade, Cuidado!\n')
   elif imc > 40:
        print('Você esta com Obesidade Morbida, Cuidado, procurar um Médico!\n')    