import re
import time

#Lista com as expressões regulares
expressoes_regulares = [
    ('Preprocessador', r'#'),        #Pré processador
    ('Comentario',   r'//.*'),       #Comentario de uma linha
    ('Num',    r'\d+(\.\d*)?'),      #Números inteiros e decimais
    ('ID',     r'[A-Za-z_]\w*(\.[A-Za-z_]\w*)?'),     #Identificadores
    ('Atribuicao',    r'='),         #Atribuição
    ('Adicao',      r'\+'),          #Adição
    ('Subtracao',     r'-'),         #Subtração
    ('Multiplicacao',     r'\*'),    #Multiplicação
    ('Divisao',    r'\/'),           #Divisão
    ('Potencia',   r'\*\*'),         #Potência
    ('Modulo',        r'%'),         #Módulo
    ('Igualdade',     r'=='),        #Igualdade
    ('Diferente',     r'!='),        #Diferença
    ('Abre_paren',    r'\('),        #Parêntese abrindo
    ('Fecha_paren',    r'\)'),       #Parêntese fechando
    ('Abre_chave',     r'\{'),       #Chave abrindo
    ('Fecha_chave',  r'\}'),         #Chave fechando
    ('Abre_colch',   r'\['),         #Colchetes abrindo
    ('Fecha_colch',  r'\]'),         #Colchetes fechando
    ('Ponto_virgula', r';'),         #Ponto e vírgula
    ('Ponto', r'\.'),                #Ponto
    ('Endereço', r'&'),              #Endereço da variável
    ('Virgula', r','),               #Virgula
    ('Maior',      r'>'),            #Maior
    ('Maior_igual',   r'>='),        #Maior ou igual
    ('Menor',        r'<'),          #Menor
    ('Menor_igual',  r'<='),         #Menor ou igual
    ('And_logico',   r'&&'),         #And/E lógico
    ('Or_logico',    r'\|\|'),       #Or/Ou lógico
    ('Not_logico',   r'!'),          #Negação lógica
    ('String',   r'"[^"]*"'),        #String
    ('Char',       r"'(.)'"),        #Constante de caractere
    ('Incremento',   r'\+\+'),       #Incremento
    ('Decremento',   r'--'),         #Decremento
    ('Ignorar',      r'[ \t]+'),     #Espaços e tabulações (ignorar)
    ('Nova_linha',   r'\n'),         #Nova linha (ignorar)
    ('Outro',  r'.'),                #Qualquer outro caractere não esperado
]

#Palavras reservadas
reserved_words = {
    'int', 'float', 'char', 'boolean', 'void',
    'if', 'else', 'for', 'while', 'do', 'continue',
    'return', 'break', 'switch', 'case', 'default', 'const',
    'static', 'struct', 'double', 'sizeof', 'typedef', 'include',
}


#Compilando as expressões regulares
token_recognition = re.compile('|'.join('(?P<%s>%s)' % pair for pair in expressoes_regulares))

#Função do analisador
def analisador(codigo):
    symbols = []
    tokens = []
    line_num = 1
    line_start = 0

    #Percorre todo o código
    for match in token_recognition.finditer(codigo):
        token_type = match.lastgroup                  #Identifica o tipo do token
        token_value = match.group(token_type)         #Retorna o valor do token

#Tratamento para classificação dos tokens
        if token_value in reserved_words:
          token_type = 'Reservada'
        if token_type == 'ID':
          if token_value not in symbols:
            symbols.append(token_value)

#Tratamento de erros e de tokens irrelevantes
        if token_type == 'Nova_linha':
            line_start = match.end()
            line_num += 1
        elif token_type == 'Ignorar':
            continue
        elif token_type == 'Comentario':
            continue
        elif token_type == 'Outro':
            if pergunta == 's':
              raise RuntimeError(f'Erro léxico: {token_value!r} inesperado na linha {line_num -1}')
            elif pergunta == 'n':
              raise RuntimeError(f'Erro léxico: {token_value!r} inesperado na linha {line_num}')
        else:
            tokens.append((token_type, token_value))

    return tokens, symbols

#Codigo pré configurado
codigo_teste = '''
#include <stdio.h>

int main() {
    printf("Hello, world!\n");
    return 0;
}

'''



#Chamada do analisador léxico
while True:
  pergunta = input("Você deseja fazer a análise léxica de um código (Em C) pré configurado? [S/N] \n").lower()
  if pergunta == "s":
    print(f"Ok! Vamos começar.")
    for i in range(3):
      time.sleep(1)
      print(f"Análise começando em {3 - i}.")
    print("\n")
    tokens, symbols = analisador(codigo_teste)
    break
  elif pergunta == "n":
    codigo_teste_user = input("Digite o código a analisar ou digite 0 para voltar: \n")
    if codigo_teste_user == "0":
      continue
    tokens, symbols = analisador(codigo_teste_user)
    break
  else:
    print("Opção inválida, digite [S/N]")

i = 0
#Exibe a tabela de simbolos
print('Tabela de Simbolos')
for id in symbols:
  i += 1
  print('-'*30)
  print(f'ID {i} = ', end=' ')
  print(f'{id}')
print('-'*30)
print('\n')

#Exibe os tokens gerados
for token in tokens:
    print(token, end=' ')
    if token[1] in symbols:
      j = 0
      for j in range(0, len(symbols)):
        if token[1] == symbols[j]:
          print(f" -> ID = {j + 1}", end='')
    print('\n')