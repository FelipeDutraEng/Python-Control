temp = dict()
dados = list()
soma = 0
while True:
    nome = str(input('Nome: ')).strip().title()
    temp['nome'] = nome
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
        if sexo in 'MF':
            break
    temp['sexo'] = sexo
    temp['idade'] = int(input('idade: '))
    dados.append(temp.copy())
    soma += temp['idade']
    seguir = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if seguir in 'N':
        break
print('-='*40)
print(f'- O grupo tem {len(dados)} pessoas.')
média = soma / len(dados)
print(f'- A média de idade é de {média:.2f} anos.')
print('- As mulheres cadastradas foram: ')
for pessoa in dados:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa["nome"]}')
print('- Lista das pessoas que estão acima da média:')
for pessoa in dados:
    if pessoa["idade"] > média:
        print(pessoa, end='')
