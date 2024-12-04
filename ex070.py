print('-'*30)
print('     LOJA SUPER BARATÃO')
print('-'*30)
caro = soma = 0
menor = 100000000000
barato = ''
continuar = 'S'
while continuar == 'S':
    produto = str(input('Nome do Produto: ')).strip().capitalize()
    valor = float(input('Preço: R$ '))
    soma += valor
    if valor > 1000:
        caro += 1
    if valor < menor:
        menor = valor
        barato = produto
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('-'*20, ' FIM DO PROGRAMA ', '-'*20)
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')