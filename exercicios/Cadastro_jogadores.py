jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    for c in range(0, tot): 
        partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp == 'N':
        break
print('-='*30)
print('cod ', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>2} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-'*40)
while True:
    dados = int(input('Quer saber os dados de que jogador? (999 p encerrar) '))
    if dados == 999:
        break
    if dados >= len(time):
        print('Erro!')
    else:
        print(f'levantamento do jogador {time[dados]["nome"]}')
        for i, g in enumerate(time[dados]['gols']):
            print(f'Na {i+1} partida fez {g} gols')
        print('-'*40)




