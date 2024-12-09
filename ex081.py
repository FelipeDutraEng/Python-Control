valores = list()
contador = 0
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    contador += 1
    seguir = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if seguir == 'N':
        break
print('-='*30)
print(f'Você digitou {contador} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista!')
