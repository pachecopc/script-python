"""
Problema: Desenvolva um programa que leia o nome, idade e sexo
de 4 pessoas. No final do programa, mostre: A média de idade do grupo.
Qual é o nome do homem mais velho. Quantas mulheres tem menos de 20 anos."""

somaidade = 0
médiaidade =0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0

for p in range(1, 5):
    print('------- {}ª Pessoa -------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1    

médiaidade = somaidade / 4   
print('A média de idade do grupo é de {}anos \n -------------'.format(médiaidade)) 
print('O home mais velho tem {} anos e se chama {}. \n -------------'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.\n -------------'.format(totmulher20))




    