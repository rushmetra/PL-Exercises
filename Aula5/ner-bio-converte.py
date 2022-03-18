# Tokenizer para a máquina de calcular 
import ply.lex as lex
import sys

# Declara the states 
states = [('Feature','exclusive')]    # qnd n tivermos a certeza, metam sempre exclusivo porque é + facil controlar

tokens = ['B','I','O']

def t_ANY_B(t):      # Esta regra vai estar viva nos dois contextos
    r''
    t.lexer.begin('Feature')

def t_O(t):
    r''
    pass


def t_Feature_O(t):
    r''
    t.lexer.begin('INITIAL')

def t_Feature_I(t):
    r''
    pass 


# Build the lexer
lexer = lex.lex()

# Variáveis de estado
lexer.features = {}

# Reading the input
for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer: 
        pass 

