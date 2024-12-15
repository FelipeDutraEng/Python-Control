dados = list()
soma = 0

while True:
    temp = dict()
    nome = str(input('Nome: ')).strip().title()
    temp['nome'] = nome
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
        if sexo in 'MF':
            break
        print('Entrada inválida! Por favor, Digite "M" ou "F".')
    temp['sexo'] = sexo
    temp['idade'] = int(input('idade: '))
    # Não precisa de '.copy()' pois estamos recriando o dicionário
    dados.append(temp)
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
        print(f'nome = {pessoa["nome"]}; sexo = {
            pessoa["sexo"]}; idade = {pessoa["idade"]}')
