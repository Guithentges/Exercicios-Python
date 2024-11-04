s = int(input("Digite quanto ganha por mes\n"))
d = int(input("Digite suas despesas fixas por mes\n"))
g = int(input("quanto vc quer guardar esse mes? (caso nao queira guardar nada digite 0)\n"))
sobra = s - d - g
print("vc tem R${} pra gastar nesse mes".format(sobra))