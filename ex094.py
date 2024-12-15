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

    while True:
        seguir = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if seguir in 'SN':
            break
        print('ERRO! Responda aepnas S ou N.')
    if seguir in 'N':
        break

print('-='*40)
print(f'A) O grupo tem {len(dados)} pessoas.')

média = soma / len(dados)
print(f'B) A média de idade é de {média:.2f} anos.')

print('C) As mulheres cadastradas foram:', end=' ')
for pessoa in dados:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa["nome"]}', end=' ')
print()

print('D) Lista das pessoas que estão acima da média:')
for pessoa in dados:
    if pessoa["idade"] >= média:
        print('')
        print(f'    nome = {pessoa["nome"]}; sexo = {
            pessoa["sexo"]}; idade = {pessoa["idade"]};')
print('<< ENCERRADO >>')
