# contador = 0   Adicionei a linha 3
# soma = 0   Adicionei a linha 3
maior = menor = soma = contador = 0
seguir = 'S'
while seguir == 'S':
    valor = int(input('Digite um valor: '))
    soma+= valor
    seguir = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if contador == 0:
        # maior = valor
        # menor = valor
        maior = menor = valor
    elif valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    contador += 1

media = soma / contador
print(f'''Você digitou {contador} número(s)
O maior valor foi {maior}
O menor valor foi {menor}
A média dos valores digitados foi {media:.2f}''')