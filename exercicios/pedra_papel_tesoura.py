from random import randint
itens = ['pedra', 'papel', 'tesoura']
comp = randint(0, 2) #aleatorio
print('='*50)
print("Pedra Papel e Tesoura, você contra o computador...")
print("Que o melhor vença!")
print("="*50)
print('''Jogadas
[0] = Pedra
[1] = Papel
[2] = Tesoura
      ''')
escolha = int(input("Sua escolha: "))
print("="*25)
print("Computador jogou {}".format(itens[comp]))
print("voce jogou {}".format(itens[escolha]))
print("="*25)

if escolha == 0:
    if comp == 0:
        print("Empate!")
    elif comp == 1:
        print("Voce perdeu :(")
    elif comp == 2:
        print("Parabens, voce ganhou!")
elif escolha == 1:
    if comp == 1:
        print("Empate!")
    elif comp == 2:
        print("Voce perdeu :(")
    elif comp == 0:
        print("Parabens, voce ganhou!")
elif escolha == 2:
    if comp == 2:
        print("Empate!")
    elif comp == 0:
        print("Voce perdeu :(")
    elif comp == 1:
        print("Parabens, voce ganhou!")

