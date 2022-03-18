# Tokenizer para converter latex em html 
# Vai sair no teste de quarta feira pelo q entendi
import ply.lex as lex
import sys
import re

# Declare the state
# Podemos fazer um estado para cada opção, mas era melhor fazer uma solução + simples
states = [('','exclusive')]

tokens = ['','','']

# Build the lexer
lexer = lex.lex()

# Reading the input
for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer: 
        pass 


# Não fiz, isto é só o esqueleto para um tokenizer genérico
