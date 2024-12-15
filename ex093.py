historico = dict()
gols = list()
nome = str(input('Nome do Jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {nome} jogou? '))

for j in range(partidas):
    gol = int(input(f'    Quantos gols na partida {j+1}? '))
    gols.append(gol)

historico['nome'] = nome
historico['gols'] = gols
historico['total'] = sum(historico['gols'])
print('-='*30)
print(historico)
print('-='*30)
for k, v in historico.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {historico["nome"]} jogou {
      len(historico["gols"])} partidas.')
for j, g in enumerate(gols):
    print(f'{"=>":>5} Na partida {j+1}, fez {g} gols.')
print(f'Foi um total de {historico["total"]} gols.')
