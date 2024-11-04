lista = []
while True:
    num = (int(input('Digite um valor: ')))
    if num in lista:
        print('ja tem na lista')
    else:
        lista.append(num)
    cont = str(input('quer continuar? [s/n]: '))
    if cont.lower() == 'n':
        break
lista.sort()
print(lista)
