# Essa foi só o Guanabara que fez
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# spar = mai = scol = 0
# for l in range(3):
#     for c in range(3):
#         matriz[l][c] = int(input(f'Digite um valor para {l}, {c}: '))
# print('-='*30)
# for l in range(3):
#     for c in range(3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#         if matriz[l][c] % 2 == 0:
#             spar += matriz[l][c]
#     print()
# print('-='*30)
# print(f'A soma dos valores pares é {spar}')
# for l in range(3):
#     scol += matriz[l][2]
# print(f'A soma dos valores da terceira coluna é {scol}')
# for c in range(3):
#     if c == 0:
#         mai = matriz[1][c]
#     elif matriz[1][c] > mai:
#         mai = matriz[1][c]
# print(f'O maior valor da segunda linha é {mai}')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para {l}, {c}: '))

print('-='*30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-='*30)

somaPares = 0
for l in range(0, 3):
    for c in range(3):
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
print(f'A soma dos valores pares é {somaPares}')

somaColuna3 = 0
for l in range(3):
    somaColuna3 += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somaColuna3}')

maior = 0
for c in range(3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')
