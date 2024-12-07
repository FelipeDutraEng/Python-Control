numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(
    input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores ({numeros})')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 pareceu na {numeros.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
pares = [n for n in numeros if n % 2 == 0]
if pares:
    print(f'Os valores pares digitados foram ', end='')
    for n in numeros:
        if n % 2 == 0:
            print(n, end=' ')
else:
    print('Não possui números pares')
