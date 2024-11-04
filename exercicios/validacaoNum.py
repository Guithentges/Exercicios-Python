def leiaint(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return n
            False
        else: 
            print('erro! Digite um numero inteiro')



n = leiaint('digite um n: ')
print(f'O num digitado foi {n}')