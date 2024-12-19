from time import sleep


def lin():
    print('-='*30)


def maior(*núm):
    lin()
    print('Analisando os valores passados...')
    maiorValor = 0
    for c in núm:
        sleep(0.3)
        print(f'{c}', end=' ')
        if c > maiorValor:
            maiorValor = c
    print(f'Foram informados {len(núm)} valores ao todo.')
    print(f'O maior valor informado foi {maiorValor}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
