import sys
import re

''' tokenizer
int = 5
op = +
int = 3
op = *
int = 21

input:
5+34*3/76

output:
int =  5
op:  +
int =  34
op:  *
int =  3
op:  /
int =  76


1      2      3
(ab) | (cd) | (ef)
m = re.search( , linha)
m.groups()

(1,2,3)

'''

exp = r'(\d+)|([+\-*/])'
pexp = re.compile(exp)


for linha in sys.stdin:
    tokens = pexp.finditer(linha)
    for t in tokens:
        if t.group(1):
            print("int = ", t.group(1))
        else:
            print("op: ", t.group(2))
