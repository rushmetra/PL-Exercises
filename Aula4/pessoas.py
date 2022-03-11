''' OUTPUT
Carvalho, J.
Almeida, S.
Monteiro, G.
Ronaldo, C.
'''

import re, sys

for linha in sys.stdin:
    linha = re.sub(r'', r'', linha)
    print(linha, end="")