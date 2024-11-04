numeros = list()
par = list()
impar = list()
for i in range(0,7):
    num = int(input(f'Digite o {i+1} numero: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
par.sort()
impar.sort()
numeros.append(par[:])
numeros.append(impar[:])
print(f'os numeros pares foram {numeros[0]}')
print(f'os numeros impares foram {numeros[1]}')