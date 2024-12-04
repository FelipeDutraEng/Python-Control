print('='*30)
print('           BANCO CEV')
print('='*30)
cedula50 = cedula20 = cedula10 = cedula1 = 0
valor = int(input('Que valor você quer sacar? R$ '))
if valor // 50:
    cedula50 = valor // 50
    valor -= cedula50 * 50
if valor != 0:
    if valor // 20:
        cedula20 = valor // 20
        valor -= cedula20 * 20
    if valor != 0:
        if valor // 10:
            cedula10 = valor // 10
            valor -= cedula10 * 10
        if valor != 0:
            if valor // 1:
                cedula1 = valor
if cedula50 > 0:
    print(f'Total de {cedula50} cédulas de R$50')
if cedula20 > 0:
    print(f'Total de {cedula20} cédulas de R$20')
if cedula10 > 0:
    print(f'Total de {cedula10} cédulas de R$10')
if cedula1 > 0:
    print(f'Total de {cedula1} cédulas de R$1')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')