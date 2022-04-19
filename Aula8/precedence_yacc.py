import ply.yacc as yacc
from precedence_lex import tokens

# def p_grammar(p):
#     """
#     Frase       : Elementos
    # Elementos   : Elementos MAI Elementos
    #             | Elementos MEN Elementos
    #             | Elementos MUL Elementos
    #             | Expressao
#     Expressao   : NUM
#     """

# 1+2*3

precedence =(
    ('left','MAI','MEN'),
    ('left','MUL','DIV'),
)
def p_frase(p):
    "Frase       : Elementos"
    parser.total += p[1]

def p_elementos_mais(p):
    "Elementos   : Elementos MAI Elementos"
    print("mais")
    p[0] = int(p[1]) + int(p[3])

def p_elementos_menos(p):
    "Elementos   : Elementos MEN Elementos"
    print("menos")
    p[0] = int(p[1]) - int(p[3])

def p_elementos_vezes(p):
    "Elementos   : Elementos MUL Elementos"
    print("vezes")
    p[0] = int(p[1]) * int(p[3])

def p_elementos_divisao(p):
    "Elementos   : Elementos DIV Elementos"
    print("dividir")
    p[0] = int(p[1]) / int(p[3])

def p_elementos_expressao(p):
    "Elementos  : Expressao"
    p[0] = p[1]

def p_expressao(p):
    "Expressao  : NUM"
    p[0] = p[1]

def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False

# Build the parser
parser = yacc.yacc()

# Read line from input and parse it
import sys
for linha in sys.stdin:
    parser.success = True
    parser.total = 0
    parser.parse(linha)
    if parser.success:
        print("Frase válida!")
        print("Resultado Total: ",parser.total)
    else:
        print("Frase inválida... Corrija e tente novamente!")