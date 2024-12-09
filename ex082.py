valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar in 'Nn':
        break
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-='*30)

print(f'A lita completa é {valores},', end=' ')
print(f'Os valores em ordem fica {valores.sort()}')
print(f'A lista de pares é {pares},', end=' ')
print(f'Os valores em ordem fica {pares.sort()}')
print(f'A lista de ímpares é {impares},', end=' ')
print(f'Os valores em ordem fica {impares.sort()}')
