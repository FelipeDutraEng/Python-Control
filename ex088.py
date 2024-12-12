from random import sample
print('-'*30)
print('      JOGO NA MEGA SENA      ')
print('-'*30)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))
repetição = 0
print('-='*4, f' SORTEANDO {jogos} JOGOS ', '-='*4)
while True:
    numeros = sample(range(1, 61), 6)
    numeros.sort()
    print(f'Jogo {repetição+1}: {numeros}')

    repetição += 1
    if repetição == jogos:
        break
print('-='*5, f' < BOA SORTE! > ', '-='*5)
