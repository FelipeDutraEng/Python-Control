from time import sleep
from random import randint

competição = dict()
print('Valores sorteados:')
sleep(1)
for j in range(4):
    competição['Jogador'] = f'Jogador{j+1}'
    competição['Dado'] = randint(1, 6)
    print(f'{"O ":>5}{competição["Jogador"]} tirou {competição["Dado"]}')
    sleep(1)
print('Ranking dos jogadores:')
