''' OUTPUT
Carvalho, J.
Almeida, S.
Monteiro, G.
Ronaldo, C.
'''

# Fiz esta expressão -> ([A-Z])\w*[\s]+([A-Z]\w*) e capturou (C)ristiano (Ronaldo)
import re, sys

for linha in sys.stdin:
    linha = re.sub(r'([A-Z])\w*[\s]+([A-Z]\w+)', r'\2, \1.', linha)
    print(linha, end="")
    
    
print("\n", end="")