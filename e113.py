def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric:
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


def leiaFloat(msg):
    try:
        ok = False
        valor = 0
        while True:
            n = str(input(msg)).strip()
            if n.isnumeric:
                valor = float(n)
                ok = True
            else:
                print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            if ok:
                break
    except KeyboardInterrupt:
        print('\033[31mUsuário preferiu não digitar esse número\033[m')
    finally:
        return valor


nInt = leiaInt('Digite um Inteiro:')
nFlo = leiaFloat('Digite um real:')
print(f'O valor inteiro digitado foi {nInt} e o real foi {nFlo}')