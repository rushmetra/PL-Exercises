'''
HTML 
<A>             texto           </A>        (hyperlink)
tag de abertura e tag de fecho    -> A (qualquer combinação de maiusculas ou minusculas)-> âncoras

<A HREF="http://www.di.uminho,pt"> texto </A>
 
'''

# Capturar os endereços dos links HTML
import sys
import re

link = r'(?i)href\s*=\s*\"([^"]+)\"'
plink = re.compile(link)

for linha in sys.stdin:
    enderecos = plink.finditer(linha)
    for e in enderecos:
        print(e.group(1))

