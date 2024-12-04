contador = soma = n = 0
while n != 999:
    soma += n
    n = int(input('Digite um valor (999 para parar): '))
    contador += 1
    if n == 999:
        break
print(f'A soma dos {contador} valores foi {soma}!')