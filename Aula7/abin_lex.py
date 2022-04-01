# ultimo exercicio da aula pl 25/03
# Gramática de Árvores Binárias 
# ()
# (22 () ())
# (22 (10 () ()) (42 () ()))
import ply.lex as lex

tokens = ['PA', 'PF', 'NUM']

t_PA = r'\('
t_PF = r'\)'
t_NUM = r'\d+'

t_ignore = " \t\n"

def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
