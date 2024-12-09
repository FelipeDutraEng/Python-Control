valores = list()
while True:
    num = (int(input('Digite um valor: ')))
    if num in valores:
        print('Valor duplicado! Não vou adicionar')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar != 'S':
        break
print('-='*30)
print('Você digitou os valores', sorted(valores))
