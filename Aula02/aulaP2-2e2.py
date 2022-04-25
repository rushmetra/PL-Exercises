import re
import sys
 
 # pra ler do stdin
f = sys.stdin


# for linha in f: (se quisesse fazer como antes)

# ler a primeira linha do input
linha1 = f.readline()
# numero de linhas q vem a seguir q quero processar  -> a linha1 neste ficheiro tem o numero de linhas (inteiro) na primeira linha
nlinhas = int(linha1)

n = 1
while nlinhas > 0:
    nlinhas = nlinhas - 1
    linha = f.readline()
    if re.search(r'^Ola$', linha): 
        print("0")
    elif re.search(r'^Ola$', linha):  
        print("1")
    elif re.search(r'Ola$', linha):
        print("2")
    else: 
        print("-1")
    n = n + 1



