pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! tente novamente...')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! tente novamente')
    if resp == 'N':
        break
media = soma / len(galera)
print('-='*15)
print(f'A) Ao todo temos {len(galera)} pessoas')
print(f'B) A média de idade das pessoas é {media:.2f}')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end='')
print()
print(f'D) as pessoas com idade acima da media foram ', end='')
for p in galera:
    if p['idade'] > media:
        print(f'{p["nome"]}', end='')
print()