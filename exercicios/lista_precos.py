lista = ('Lapis', 1.75,
         'borracha', 2,
         'cadernos', 15.9,
         'estojo', 25,
         'mochila', 120,
         'canetas', 22.3)
print('-'*40)
print(f'{"Lista de preços":^40}')
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    if pos % 2 == 1:
        print(f'R${lista[pos]:>7.2f}')
print('-'*40)