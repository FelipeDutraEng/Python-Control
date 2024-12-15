from datetime import date

dadosAponsentadoria = dict()

anoAtual = date.today().year

dadosAponsentadoria['nome'] = str(input('Nome: ')).strip().title()

nascimento = int(input('Ano de Nascimento: '))
dadosAponsentadoria['idade'] = anoAtual - nascimento

ctps = int(input('Carteira de Trabalho (0 não tem): '))
dadosAponsentadoria['ctps'] = ctps
if ctps != 0:
    anoContrato = int(input('Ano de contratação: '))
    dadosAponsentadoria['contratação'] = anoContrato
    salário = float(input('Salário: R$ '))
    dadosAponsentadoria['salário'] = salário
    dadosAponsentadoria['aposentadoria'] = (
        35 - (anoAtual - anoContrato)) + dadosAponsentadoria['idade']
print('-='*30)
for k, v in dadosAponsentadoria.items():
    print(f'  - {k} tem o valor {v}')
