from time import sleep
def contador(i, f, p):
    print(f'contagem de {i} ate {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=" ", flush=True) #flush p o sleep funcionar
            sleep(0.5)
            cont += p
        print('Fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=" ", flush=True) #flush p o sleep funcionar
            sleep(0.5)
            cont -= p
        print('Fim')
    

contador(1, 10, 1)
contador(10, 0, 2)
i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))
contador(i, f, p)
        