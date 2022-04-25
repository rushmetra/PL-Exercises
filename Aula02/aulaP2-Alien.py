import re
import sys 

"""
Enunciado:
Tem que começar com '_' ou '.'
Seguido de um numero
Mais qq coisa sobre as letras
Tem que acabar com letras ou com underscore '-'

"""


# Expressão regular para o Alien Username do problema1: 
p = re.compile(r'^(_|\.)\d+[a-zA-Z]{3,}_?$')

for linha in sys.stdin:
    if p.match(linha):
        print("VÁLIDO")
    else:
        print("INVÁLIDO")