# contador = 0
# n= 0
# soma = 0
n = soma = contador = 0
print('Número 999 para o sistema')
n = int(input('Digite um valor : '))
while n != 999:
    contador += 1
    soma += n
    n = int(input('Digite um valor : '))
print(f'Você digitou {contador} números')
print(f'A soma dos número digitados é igual a {soma}')