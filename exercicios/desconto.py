preco = float(input('Digite o preço do produto em R$ :'))
des = int(input('Quantos por cento de desconto?'))
vd = preco - (preco*des/100)
print('O produto vai sair por {:.2f} R$'.format(vd))