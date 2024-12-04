from random import randint
print('-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)
contador = computador = 0
victory = False
while not victory:
    num = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    computador = randint(1,10)
    soma = num + computador
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print('-'*20)
    print(f'Você jogou {num} e o computador {computador}. Total de {soma} deu {resultado}')
    print('-'*20)
    if escolha == 'P' and resultado == 'PAR' or escolha == 'I' and resultado == 'ÍMPAR':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('-='*20)
        contador +=1
    else:
        print('Você PERDEU!')
        print('-='*20)
        print(f'GAME OVER! Você venceu {contador} vezes.')
        break
