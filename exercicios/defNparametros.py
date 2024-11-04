def maior(* num):
    cont = maior = 0
    print('-='*20)
    for n in num:
        if n > maior:
            maior = n
        cont += 1
        print(f'{n}', end=' ')
    print()
    print(f'foram contados {cont} numeros e o maior foi {maior}')
    print('-='*20)

maior(1, 5, 3, 7)
maior(6, 8, 1)
maior(1)
print('Fim')