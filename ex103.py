def lin(n):
    print('-'*n)


def ficha(str, gols=0):
    lin(30)
    if str == '':
        str = '<desconhecido>'

ficha(input('Nome do Jogador: '))
ficha(gols) = int(input('Número de Gols: '))

print(f'O jogador {ficha(str)} fez {ficha(gols)} no campeonato.')