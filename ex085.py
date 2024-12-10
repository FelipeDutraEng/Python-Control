num = [[], []]
for v in range(7):
    valor = int(input(f'Digite o {v+1}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {sorted(num[1])}')
