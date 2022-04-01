import ply.yacc as yacc 
from calc_lex import tokens, literals

def p_Comandos_Lista(p):
    "Comandos : Comandos Comando"

def p_Comandos_Simples(p):
    "Comandos : Comando"

def p_Comando_Atrib(p):
    "Comando : id '=' Exp" 
    p.parser.registos[p[1]] = p[3]

def p_Comando_Escrita(p):
    "Comando : '!' Exp"
    print(p[2])

def p_Comando_Leitura(p):
    "Comando : '?' id"
    


def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False

# Build the parser
parser = yacc.yacc()
# Variáveis de estado 
parser.registos = {}


# Read line from input and parse it
import sys
for linha in sys.stdin:
    parser.success = True
    parser.parse(linha)
    if parser.success:
        print("Frase válida: ", linha)
    else:
        print("Frase inválida... Corrija e tente novamente!")