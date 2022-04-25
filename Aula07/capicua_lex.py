'''
Aula 7: 01/04/2022
 
Gramática para reconhecer capicuas.
'''

import ply.lex as lex

tokens = ['z', 'u']

t_z = r'0'
t_u = r'1'

t_ignore = " \t\n"

def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
