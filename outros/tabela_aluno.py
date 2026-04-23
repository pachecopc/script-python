def ler_notas(nome):
    notas = []
    for i in range(1, 4):
        nota = float(input(f'Informe a {i}ª nota do aluno {nome}: '))
        notas.append(nota)
    media = sum(notas) / 3
    return notas, media

def definir_status(media):
    if media >= 7:
        return 'Aprovado'
    elif media >= 5:
        return 'Recuperação'
    else:
        return 'Reprovado'


alunos = []

for i in range(1, 4):
    nome = input(f'Informe o nome do {i}º aluno: ').capitalize()
    notas, media = ler_notas(nome)
    status = definir_status(media)
    alunos.append({'nome': nome, 'notas': notas, 'media': media, 'status':status})

print('\n+-----------------------------------------------------------------------+')    
print('| Nome do Aluno      |  Média      |  Status                                 |')
print('+-------------------------------------------------------------------------+')   

for aluno in alunos:
    print(f'|  {aluno["nome"]:<16}  |  {aluno["media"]:<7.2}  |  {aluno["status"]:<16}  |')
    print('+--------------------------------------------------------------------------+')    

    