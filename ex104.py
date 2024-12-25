def leiaInt(n):
  n = 0
  if n != int:
    return(print('\033[31mERRO! Digite um número inteiro válido.\033[m'))


n = leiaInt('Digite um número: ')
resp = print(f'Você acabou de digitar o número{n}')
