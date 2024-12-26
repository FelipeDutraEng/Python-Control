def lin(n):
    print('-'*n)


def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


lin(30)
n = input('Nome do Jogador: ').strip()
g = input('Número de Gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0

if n == '':
    ficha(gol=g)
else:
    ficha(n, g)
