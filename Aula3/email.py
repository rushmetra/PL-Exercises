''' 
Email
user@dom.top-dom


user - alfanuméricos ou alguns carateres especiais: '-','.', etc;
O primeiro e último caráter não pode ser um caráter especial;
Não pode haver 2 carateres especiais consecutivos
dom - alfanuméricos e hífen
top-dom - alfanuméricos e hífen com 2 ou mais carateres

Criar um programa em Python que:

1. Apanha os emails presentes no dataset;
2. Ordena-os alfabeticamente;
3. Como resultado, 


emails.txt : (output)
1. invalido
2. valido
3. invalido
4. invalido
5. invalido
6. invalido
7. valido
'''

import sys
import re

# email = r'\d+^(_|.)\d+'
email = r'(\w+[\-.]?\w+)+@(\w+\-?\w+\.)+(\w+\-?\w+)+$'
pemail = re.compile(email)

for (n,linha) in enumerate(sys.stdin):
    m = pemail.search(linha)
    if m:
        print(n, ' :: ', "VÁLIDO", " :: ", m.group())
    else:
        print(n, ' :: ', "INVÁLIDO")