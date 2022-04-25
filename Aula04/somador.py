'''
Somador on/off:
1. De ínicio o somador está ON;
2. Se apanhar ON -> passa a ON;
3. Se apanhar OFF -> passa a OFF;
4. Se apanhar \dt -> Se on soma
                     Se off não faz nada
5. Se apanhar = -> imprime a soma
'''

# Tokenizer para a parentesis
import ply.lex as lex

tokens = ["ON", "OFF", "NUM", "PRINT"]

def t_ON(t):
    r'[Oo][Nn]'
    t.lexer.semaforo = True

def t_OFF(t):
    r'[Oo][Ff][Ff]'
    t.lexer.semaforo = False


def t_NUM(t):
    r'\d+'
    if t.lexer.semaforo:
        t.lexer.soma = t.lexer.soma + int(t.value)

def t_PRINT(t):
    r'='
    print("Soma: ", t.lexer.soma)

# carateres a ignorar 
t_ignore = '\n\t '

def t_error(t):
   # print(f"ERROR: Illegal character '{t.value[0]}' at position ({t.lineno}, {t.lexpos})")
    t.lexer.skip(1)

# analisador léxico 
lexer = lex.lex()
# Definição do estado
lexer.semaforo = True
lexer.soma = 0

import sys 

for line in sys.stdin:
    lexer.somador = 0
    lexer.input(line)
    for tok in lexer:
        print(tok)