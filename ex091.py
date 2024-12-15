from time import sleep
from random import randint
from operator import itemgetter

competição = list()
print('Valores sorteados:')

for j in range(4):
    jogador = {'Jogador': f'jogador{j+1}', 'Dado': randint(1, 6)}
    competição.append(jogador)
    print(f'{"O ":>5}{jogador["Jogador"]} tirou {jogador["Dado"]}')
    sleep(1)

print('== Ranking dos jogadores ==')

ranking = sorted(competição, key=itemgetter('Dado'), reverse=True)

for i, jogador in enumerate(ranking, start=1):
    print(f'{i}º lugar: {jogador["Jogador"]} com {jogador["Dado"]}')
    sleep(1)
