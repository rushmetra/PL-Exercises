import re 
import sys

"""
Problema 3: Latitude e Longitude

1. Cada par de coordenadas deverá seguir a forma: (X,Y) onde X e Y são números decimais (parte inteira e uma parte decimal opcional)
2. O valor de X deverá estar entre -90 e +90
3. O valor de Y deverá estar entre -180 e +180
4. Quer X quer Y podem ser opcionalmente precedidos por um sinal + ou -
5. Tem de haver um espaço entre Y e a vírgula precedente
6. Não há espaço entre X e o parentesis precedente nem entre Y e o paresentises que se lhe segue
7. Não poderá haver zeros deesnecessários à esquerda nas partes inteiras

VÁLIDOS
(75, 180)
(+90.0, -147.45)
(+90, +180)

INVÁLIDOS
(75, 280)
(+190.0, -145,45)
(+90, +180.2)
(+90, +180.00000000000000)
"""

coordenadas = r'\([+\-]?[1-9]?\d(\.\d+)?, [+\-]?(1[0-8]\d[1-9]?\d)(\.\d+)?\)'
# r'\((\x|-)?'

p = re.compile(coordenadas)

for linha in sys.stdin:
    if p.match(linha):
        print("VÁLIDO")
    else:
        print("INVÁLIDO")