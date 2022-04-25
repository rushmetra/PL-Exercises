import ply.yacc as yacc 
from abin_lex import tokens

def p_ABin_vazia(p):
    "ABin : PA PF"
    p[0] = "null"

def p_ABin(p):
    "ABin : PA NUM ABin ABin PF"
    print("{")
    print("\t\"root\": ", p[2], ",")
    print("\t\"left\": ", p[3], ",")
    print("\t\"right\": ", p[4])
    print("}")
    

def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False

# Build the parser
parser = yacc.yacc()

# Read line from input and parse it
import sys
for linha in sys.stdin:
    parser.success = True
    parser.parse(linha)
    if parser.success:
        print("Frase válida: ", linha)
    else:
        print("Frase inválida... Corrija e tente novamente!")