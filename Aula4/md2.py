# MD to HTML converter 
import sys, re

for linha in sys.stdin:
    linha = re.sub(r'\*\*(.+)\*\*', r'<b>\1</b>', linha)
    linha = re.sub(r'__(.+)__', r'<i>\1</i>', linha)
    print(linha, end="")