# n = int(input('Digite a quantidade de número que deseja ver da sequencia de fibonacci: '))
# fi = 0
# fi_antigo = 0
# contador = 0
# while contador < n:
#     if contador == 0:
#         print(fi, end='-')
#         print(contador)
#         contador += 1
#         fi += 1
#     elif contador == 1:
#         print(fi, end='-')
#         print(contador)
#         contador += 1
#     else:
#         fi_antigo = fi
#
#         print(fi,end=' fi ')
#         print(contador, 'contador')
#         contador += 1
#         fi += fi_antigo

# NÃO CONSEGUE FINALIZAR

# RESOLUÇÃO GUANABARA

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1, t2),end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' - FIM')
print('~'*30)
