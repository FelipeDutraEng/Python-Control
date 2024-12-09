valores = list()
pares = list()
impares = list()
while True:
    num = int(input('Digite um número: '))
    valores.append(num)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-='*30)

print(f'A lita completa é {valores},', end=' ')
valores.sort()
print(f'Os valores em ordem fica {valores}')
print(f'A lista de pares é {pares},', end=' ')
pares.sort()
print(f'Os valores em ordem fica {pares}')
print(f'A lista de ímpares é {impares},', end=' ')
impares.sort()
print(f'Os valores em ordem fica {impares}')
