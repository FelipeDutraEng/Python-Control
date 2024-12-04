pessoaMais18 = idade = homens = mulheresMenos20 = 0
continuar = 'S'
while continuar == 'S':
    print('-'*30)
    print('   CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        pessoaMais18 += 1
    if sexo == 'M':
        homens += 1
    if idade > 20 and sexo == 'F':
        mulheresMenos20 += 1
    print('-'*30)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('='*20, ' FIM DO PROGRAMA ', '='*20)
print(f'Total de pessoas com mais de 18 anos: {pessoaMais18}')
print(f'Ao total temos {homens} homens cadastrados')
print(f'E temos {mulheresMenos20} mulheres com menos de 20 anos')