# ------------------------------------------------------------
# recdesc-par.py
#
# Parser recursivo descendente para a linguagem dos parentesis:
# ()
# (())
# ()(()())
# ------------------------------------------------------------
import ply.lex as lex

tokens = ('PA','PF')

t_PA   = r'\('
t_PF   = r'\)'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
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


def rec_S():
    global prox_simb
    if prox_simb.type == 'PA':
        rec_term('PA')
        rec_S()
        rec_term('PF')
        rec_S()
    elif prox_simb.type == 'FIM' or prox_simb.type == 'PF':
        pass
    else:
        parserError(prox_simb)    


def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    rec_S()
    print("That's the end...")


# Programa de teste
linha = input("Introduza uma lista: ")
# Teste do tokenizer
# lexer.input(linha)
# for tok in lexer:
#     print(tok)
#     print(tok.type, tok.value, tok.lineno, tok.lexpos)
rec_Parser(linha)
    




