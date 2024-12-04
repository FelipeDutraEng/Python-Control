print('='*30)
print('           BANCO CEV')
print('='*30)
cedulas = [50, 20, 10, 1]
resultado = {}
valor = int(input('Que valor você quer sacar? R$ '))
for cedula in cedulas:
    if valor // cedula > 0:
        resultado[cedula] = valor // cedula
        valor %= cedula
for cedula, quantidade in resultado.items():
    print(f'Total de {quantidade} cédulas de R${cedula}')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')