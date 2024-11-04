def notas(*n, sit=False):
    maior = soma = cont = 0
    menor = 999
    resp = dict()
    for v in n:
        if v > maior:
            maior = v
        if v < menor:
            menor = v
        soma += v
        cont += 1
    media = soma/cont
    resp['total'] = len(n)
    resp['maior'] = maior
    resp['menor'] = menor
    resp['media'] = media
    if sit == True:
        if media >= 7:
            resp['situacao'] = 'Aprovado por media'
        elif  5 <= media < 7:
            resp['situacao'] = 'Aprovado'
        else:
            resp['situacao'] = 'Reprovado'
    return resp



resp = notas(7, 10, 8.8, sit=True)
print(resp)