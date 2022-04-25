import re
import sys

"""
Enunciado - Problema 4: Mátriculas de outro mundo
Num país algures, as matrículas seguem os seguintes requisitos:

1. uma matricula tem 8 digitos
2. 8 digitos tao dividos em 4 partes iguais de 2 digitos por um separador que pode ser um '...','-' ou ':'
3. cada matricula so pode ter uma especie de separador
4. os separadores têm de ter dígitos antes e depois, não há espaços

Exemplos válidos:
88-77-66-55
01...03...44...19
00:11:21:12
Exemplos inválidos:
0A-01-01-01
11:12-13-14
"""

p = re.compile(r'^((\d\d-){3}|(\d\d:){3}|(\d\d\.\.\.){3})\d\d')

""" Ver se são válidas ou não
for linha in sys.stdin:
    if p.match(linha):
        print("VÁLIDO")
    else:
        print("INVÁLIDO")
"""

# Isto era para calcular o número de mátriculas num input, consigo usar qnd passo um ficheiro mas ao usar o input não funciona tao bem
matriculas = 0
for linha in sys.stdin:
    lista = p.findall(linha)
    if lista:
            matriculas = matriculas + len(lista)
    print(matriculas)
    