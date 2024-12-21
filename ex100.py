from random import randint
from time import sleep
numeros = []

# função sorteio irá sortear 5 números de 1 a 10 com um sleep de 0.5 segundos.


def sorteia():
    for c in range(5):
        c = randint(1, 10)
        numeros.append(c)
    print(f'Sorteando {len(numeros)} valores da lista: ', end='')
    for c in numeros:
        print(f'{c}', end=' ')
        sleep(0.5)
    print('PRONTO!')


def somaPar():
    par = 0
    for c in numeros:
        if c % 2 == 0:
            par += c
    print(f'Somando os valores de {numeros}, temos {par}')


sorteia()
somaPar()
