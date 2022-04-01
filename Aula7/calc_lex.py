'''
Aula 7: 01/04/2022
 
calculadora 
'''

import ply.lex as lex
literals = ['+', '-', '*', '/', '(', ')', '!', '=', '?']

tokens = ['id', 'num', 'DUMP']

t_id = r'[_a-zA-Z]\w*'
t_DUMP = r'!!'

def t_num(t):
    r'\d+'
    t.value = int (t.value)
    return t 

t_ignore = " \t\n"

def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()