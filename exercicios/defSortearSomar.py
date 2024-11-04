from random import randint
numeros = list()
def sortear(num):
    print(f'Sorteando {num} numeros')
    for i in range(0, num):
        numeros.append(randint(0, 9))
    print(numeros)

def somar(lista):
    cont = 0
    for i in lista:
        if i % 2 == 0:
            cont += i
    print(f'A soma dos numeros pares foi {cont}')

sortear(5)
somar(numeros)