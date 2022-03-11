# Tokenizer para a parentesis
import ply.lex as lex

tokens = ["PA", "PF"]

def t_PA(t):
    r'\('
    t.lexer.af += 1
    return t

def t_PF(t):
    r'\)'
    t.lexer.af -= 1
    if t.lexer.af < 0:
        print("ERRO: parentesis a fechar sem ter aberto!")
    return t

# carateres a ignorar 
t_ignore = '\n\t '

def t_error(t):
    print(f"ERROR: Illegal character '{t.value[0]}' at position ({t.lineno}, {t.lexpos})")
    t.lexer.skip(1)

# analisador léxico 
lexer = lex.lex()
# Definição do estado
lexer.af = 0

import sys 

for line in sys.stdin:
    lexer.af = 0
    lexer.input(line)
    for tok in lexer:
        print(tok)