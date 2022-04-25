# ------------------------------------------------------------
# recdesc.py
#
# Parser recursivo descendente para listas de inteiros:
# []
# [8]
# [4,5,6,7]
# ------------------------------------------------------------
import ply.lex as lex

tokens = ('NUM','PA','PF','VIRG')

t_NUM    = r'\d+'
t_PA   = r'\['
t_PF   = r'\]'
t_VIRG  = r','

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Erro Léxico: '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

###########################
prox_simb = ('Erro', '', 0, 0)

def parserError(simb):
    print("Erro Sintático: ", simb)

def rec_term(simb):
    global prox_simb
    if prox_simb.type == simb:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)

def rec_ElemCont():
    global prox_simb
    if prox_simb.type == 'VIRG':
        rec_term('VIRG')
        rec_Elems()
    elif prox_simb.type == 'PF':
        pass
    else:
        parserError(prox_simb)

def rec_Elem():
    rec_term('NUM')

def rec_Elems():
    rec_Elem()
    rec_ElemCont()

def rec_LCont():
    global prox_simb
    if prox_simb.type == 'PF':
        rec_term('PF')
    elif prox_simb.type == 'NUM':
        rec_Elems()
        rec_term('PF')
    else:
        parserError(prox_simb)

def rec_Lista():
    rec_term('PA')
    rec_LCont()
    


def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    rec_Lista()
    print("That's the end...")


# Programa de teste
linha = input("Introduza uma lista: ")
# Teste do tokenizer
# lexer.input(linha)
# for tok in lexer:
#     print(tok)
#     print(tok.type, tok.value, tok.lineno, tok.lexpos)
rec_Parser(linha)
    




