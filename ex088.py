from random import randint
from time import sleep
print('-'*30)
print('      JOGO NA MEGA SENA      ')
print('-'*30)
lista = list()
jogos = list()
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 0
print('-='*4, f' SORTEANDO {quant} JOGOS ', '-='*4)
while quant > tot:
    contador = 0
    while True:
        numeros = randint(1, 60)
        if numeros not in lista:
            lista.append(numeros)
        contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for l, s in enumerate(jogos):
    print(f'Jogo {l+1}: {s}')

print('-='*5, f' < BOA SORTE! > ', '-='*5)
