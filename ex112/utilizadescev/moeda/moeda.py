def aumentar(preço, taxa, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço, taxa, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res) 


def dobro(preço, formato=False):
    res = preço * 2
    return res
    return res if formato is False else moeda(res)


def metade(preço, formato=False):
    res = preço / 2
    return res
    return res if formato is False else moeda(res) 


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do Preço: \t{dobro(preço, True)}')
    print(f'Metade do Preço: \t{metade(preço, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-'*30)