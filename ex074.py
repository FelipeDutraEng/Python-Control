# from random import randint
# numeros = tuple(randint(1, 12) for _ in range(5))
# print(f' Os valores sorteados foram: {numeros}')
# print(f'O maior valor sorteado foi {max(numeros)}')
# print(f'O menor valor sorteado foi {min(numeros)}')


# Forma que o Guanabara fez abaixo

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
