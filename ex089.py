boletim = list()
aluno = list()

while True:
    aluno.append(str(input('Nome: ')))
    nota01 = float(input('Nota 1: '))
    nota02 = float(input('Nota 2: '))
    média = (nota01 + nota02) / 2
    aluno.append(nota01)
    aluno.append(nota02)
    aluno.append(média)
    boletim.append(aluno[:])
    aluno.clear()
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*25)
for a, i in enumerate(boletim):
    print(f'{a:<4}{i[0]:<10}{i[3]:>8.1f}')
print('-'*30)

while True:
    idAluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if idAluno == 999:
        break
    for a, i in enumerate(boletim):
        if idAluno == a:
            print(f'Notas de {i[0]} são [{i[1]}, {i[2]}]')
