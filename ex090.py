boletim = dict()
boletim['Nome'] = str(input('Nome: ')).strip()
boletim['Média'] = float(input(f'Média de {boletim["Nome"]}: '))
if boletim['Média'] >= 7:
    boletim['Situação'] = 'Aprovado'
else:
    boletim['Situação'] = 'Reprovado'
for k, v in boletim.items():
    print(f'{k} é igual a {v}')
