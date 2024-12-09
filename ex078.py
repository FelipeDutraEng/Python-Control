valores = []
maior = 0
menor = 0

for p in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {p}: ')))
    if p == 0:
        maior = menor = valores[p]
    else:
        if valores[p] > maior:
            maior = valores[p]
        if valores[p] < menor:
            menor = valores[p]

print('-='*30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')

for p, v in enumerate(valores):
    if v == maior:
        print(f'{p}...', end='')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')

for p, v in enumerate(valores):
    if v == menor:
        print(f'{p}...', end='')
