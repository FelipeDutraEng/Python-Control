def lin():
    print('-='*30)


def contagem(a, b, c):
    lin()
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if c == 0:
        c = 1
    if a > b and c > 0:
        c *= -1
    for cont in range(a, b, c):
        print(cont, end=' ')
    print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)
lin()
print('Agora é sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contagem(a, b, c)