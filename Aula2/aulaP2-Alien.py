import re
import sys 

# Expressão regular para o Alien Username do problema1: 
p = re.compile(r'^(_|\.)\d+[a-zA-Z]{3,}_?$')

for linha in sys.stdin:
    if p.match(linha):
        print("VÁLIDO")
    else:
        print("INVÁLIDO")