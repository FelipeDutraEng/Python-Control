dados = list()
cod = 0
while True:
    jogadores = dict()
    print('-'*40)
    jogadores['cod'] = cod

    nome = str(input('Nome do Jogador: ')).strip().title()
    jogadores['nome'] = nome

    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    jogadores['jogos'] = partidas
    gols = list()
    total = 0

    for jogos in range(partidas):
        gol = int(input(f'Quantos gols na partida {jogos+1}? '))
        total += gol
        gols.append(gol)
        jogadores['gols'] = list(gols)
        jogadores['total'] = total
    dados.append(jogadores)

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            cod += 1
            break
        print('Comando inválido! Digite "S" ou "N".')
    if continuar in 'N':
        break

print('-='*30)
print(f'cod {"nome":<20}{"gols":<20}{"total":>2}')
print('-'*30)
for jogador in dados:
    print(f'{jogador["cod"]:>3} {jogador["nome"]:<20}{
          str(jogador["gols"]):<20}{jogador["total"]:>2} ')
print('-'*30)
while True:
    mostrar = int(input('Mostrar dados de qual jogador? '))
    if mostrar == 999:
        break

    if mostrar >= len(dados) or mostrar < 0:
        print(f'ERRO! Não existe jogador com Código {
              mostrar}! Tente novamente')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {dados[mostrar]["nome"]}')
        for i, gols in enumerate(dados[mostrar]["gols"]):
            print(f'No jogo {i} fez {gols} gols.')

    print('-'*30)
print('<< VOLTE SEMPRE >>')
