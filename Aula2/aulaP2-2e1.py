import sys



n = 1
for linha in sys.stdin:
    print(n, ": ", linha, end="")
    n = n + 1

# cat input.txt | python3.9  ficheiro.py        -> pra ler do file
