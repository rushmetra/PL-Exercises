import ply.yacc as yacc
from exercicio2_lex import tokens


# def p_grammar(p):
#     """
#     Frase       : Elementos
    # Elementos : Elemento 
    #            | ELemento VIR Elementos
    #           ´
    # ELemento   : NAME CHAVAVRIR Elementos CHAVFECHAR  
    #             | NAME 
    #             | empty
#     """

# PL { doc {} , aulas { { f1,f2,f3} } }
# PL { doc {} , aulas { { f1,f2,f3} } }


precedence =(
    ('left','VIRG'),
    ('left','NAME','CHAV_ABRIR','CHAV_FECHAR'),
)

def p_frase(p):
    "Frase       : Elementos"

def p_elementos_varios(p):
    "Elementos   : Elementos VIRG Elementos"

def p_elementos_unico(p):
    "Elementos   : Elemento"


def p_elemento_pasta(p):
    "Elemento   : NAME CHAV_ABRIR Elementos CHAV_FECHAR"
    print("pasta",p[1],";")

def p_elemento_ficheiro(p):
    "Elemento   : NAME "
    print("ficheiro",p[1],";")

def p_elemento_vazio(p):
    "Elemento  : "

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
    else:
        print("Frase inválida... Corrija e tente novamente!")