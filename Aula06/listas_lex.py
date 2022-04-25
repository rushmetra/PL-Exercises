# Listas 
# Feito no papel

import ply.lex as lex

tokens = ['PA', 'PF', 'NUM', 'VIRG']

t_PA = r'\['
t_PF = r'\]'
t_NUM = r'\d+'
t_VIRG = r','

t_ignore = " \t\n"

def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
