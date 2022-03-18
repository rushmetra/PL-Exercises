# Tokenizer para a máquina de calcular 
import ply.lex as lex
import sys

# Declare the state

states = [('COM','exclusive')]

tokens = ['BCOM','ECOM','TEXT']

# BegingComentario , EndComentario, Text é o content

def t_BCOM(t):
    r'<!--'
    t.lexer.begin('COM')

def t_TEXT(t):
    r'.|\n'
    print(t.value, end="")

def t_COM_ECOM(t):
    r'-->'
    t.lexer.begin('INITIAL')

def t_COM_TEXT(t):
    r'.|\n'
    pass

# Build the lexer
lexer = lex.lex()

# Reading the input
for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer: 
        pass 
