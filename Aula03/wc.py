# It can return the number of lines in a file, the number of characters in a file and the number of words in a file
# how to teste/compare      ------> (usando pipes)          ls -la | wc 
import sys
import re

# f = sys.stdin
# texto = f.read()

pal = r'[A-Za-z]+'     # assim nao apanha as palavras todas mas ta valendo
ppal = re.compile(pal)

chars = 0
pals = 0
linhas = 0

for linha in sys.stdin:
    pals =  pals + len(ppal.findall(linha))
    linhas = linhas + 1
    chars = chars + len(linha)

print(linhas, pals, chars)