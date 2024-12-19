def título(msg):
    print(f'{msg:^30}')
    print('-'*30)


# def área():
#     largura = float(input('LARGURA (m): '))
#     comprimento = float(input('COMPRIMENTO (m): '))
#     área = largura * comprimento
#     print(f'A área de um terreno {largura}x{comprimento} é de {área:.1f}m²')


# título('Controle de Terrenos')
# área()

def área(largura, comprimento):
    área = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {área}m²')


título('Controle de Terrenos')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

área(largura, comprimento)