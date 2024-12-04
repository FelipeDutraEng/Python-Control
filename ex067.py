n = 0
while n >= 0:
    print('-'*30)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n < 0:
        break
    for c in range (1,11):
        mult = n * c
        print(f'{n} X { c:2} = {mult}')




print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')