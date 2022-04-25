# PL { doc {} , aulas { { f1,f2,f3} } }
# PL { doc {} , aulas { { f1,f2,f3} } }

import ply.lex as lex

tokens = ['CHAV_ABRIR','CHAV_FECHAR','VIRG','NAME']

t_CHAV_ABRIR = r'{'
t_CHAV_FECHAR = r'}'
t_VIRG = r','
t_NAME = r'[a-zA-Z0-9\-]+'


t_ignore = " \t\n"

def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

