valores = list()
for p, v in enumerate(range(5)):
    num = int(input('Digite um valor: '))
    if p == 0:
        print('Adicionado ao final da lista...')
        valores.append(num)
    elif p == 1:
        if num > valores[0]:
            valores.append(num)
            print('Adicionado ao final da lista...')
        else:
            valores.insert(0, num)
            print('Adicionado no posição 0 da lista...')
    elif p == 2:
        if num > valores[1]:
            valores.append(num)

        elif valores[0] < num < valores[1]:
            valores.insert(1, num)
            print('Adicionado no posição 1 da lista...')
        else:
            valores.insert(0, num)
            print('Adicionado no posição 0 da lista...')
    elif p == 3:
        if num > valores[2]:
            valores.append(num)
            print('Adicionado ao final da lista...')
        elif valores[1] < num < valores[2]:
            valores.insert(2, num)
            print('Adicionado no posição 2 da lista...')
        elif valores[0] < num < valores[1]:
            valores.insert(1, num)
            print('Adicionado no posição 1 da lista...')
        else:
            valores.insert(0, num)
            print('Adicionado no posição 0 da lista...')
    else:
        if num > valores[3]:
            valores.append(num)
            print('Adicionado ao final da lista...')
        elif valores[2] < num < valores[3]:
            valores.insert(3, num)
            print('Adicionado no posição 3 da lista...')
        elif valores[1] < num < valores[2]:
            valores.insert(2, num)
            print('Adicionado no posição 2 da lista...')
        elif valores[0] < num < valores[1]:
            valores.insert(1, num)
            print('Adicionado no posição 1 da lista...')
        else:
            valores.insert(0, num)
            print('Adicionado no posição 0 da lista...')
print('-='*30)
print(f'Os valores digitados em ordem foram {valores}')
