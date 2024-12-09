valores = []
for p, v in enumerate(range(5)):
    num = int(input('Digite um valor: '))
    if p == 0 or num > valores[-1]:
        print('Adicionado ao final da lista...')
        valores.append(num)
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {valores}')
