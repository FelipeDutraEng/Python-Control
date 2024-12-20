from datetime import datetime
anoAtual = datetime.now().year

def voto(nascimento):
    idade = anoAtual - nascimento
    if 17 < idade < 70:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    elif idade >= 70 or idade >= 16:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        print(f'Com {idade} anos: NÃO VOTA.')


def lin(num):
    print('-'*num)


lin(30)
voto(int(input('Em que ano você nasceu? ')))

