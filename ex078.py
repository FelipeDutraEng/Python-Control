valores = list()
maior = 0
posicaoMaior = 0
menor = 10000
posicaoMenor = 0
for p, v in enumerate(range(0, 5)):
    valores.append(int(input(f'Digite um valor para a posição {p}: ')))
print('-='*30)
print(f'Você digitou os valores {valores}')
for p, v in enumerate(valores):
    if v > maior:
        maior = v
        posicaoMaior = p
    elif v < menor:
        menor = v
        posicaoMenor = p
print(f'O maior valor digitado foi {maior} nas posições {posicaoMaior}...')
print(f'O menor valor digitado foi {menor} nas posições {posicaoMenor}...')
