# Tokenizer para converter pra estrutura que o professor pediu, foi um dos trabalhos práticos do ano passado
import ply.lex as lex
import sys
import re

# Declara the states 
states = [('Feature','exclusive')]    # qnd n tivermos a certeza, metam sempre exclusivo porque é + facil controlar

tokens = ['B','I','O']

t_ANY_ignore = "\n"    # mesma regra pra todos os contextos

def t_ANY_error(t):
    t.lexer.skip(1)

def t_B(t):      
    r'B-.+'
    conteudo = t.value[2:]   # Isto retira me o q está na pos 0 e na pos 1 (B-)
    partes = re.split(r'\s+', conteudo)
    t.lexer.tipo = partes[0]
    t.lexer.buffer = partes[1]
    t.lexer.begin('Feature')


def t_O(t):
    r'O.+'
    pass


def t_Feature_O(t):
    r'O.+'
    if lexer.tipo in t.lexer.features.keys():      # pergunta se o tipo já existe no dicionario 
        t.lexer.features[t.lexer.tipo].append(t.lexer.buffer)     # selecionar a lista e fazer lhe append se ja existe
    else: # entrada não existe no dicionário
        t.lexer.features[t.lexer.tipo] = [t.lexer.buffer]          # fazer atribuição
    t.lexer.begin('INITIAL')

def t_Feature_I(t):
    r'I-.+'
    partes = re.split(r'\s+', t.value)
    t.lexer.buffer += " " + partes[1]
    pass 

def t_Feature_B(t):
    r'B-.+'
    if lexer.tipo in t.lexer.features.keys():      # pergunta se o tipo já existe no dicionario 
        t.lexer.features[t.lexer.tipo].append(t.lexer.buffer)     # selecionar a lista e fazer lhe append se ja existe
    else: # entrada não existe no dicionário
        t.lexer.features[t.lexer.tipo] = [t.lexer.buffer] 
    r'B-.+'
    conteudo = t.value[2:]   # Isto retira me o q está na pos 0 e na pos 1 (B-)
    partes = re.split(r'\s+', conteudo)
    t.lexer.tipo = partes[0]
    t.lexer.buffer = partes[1]


# Build the lexer
lexer = lex.lex()

# Variáveis de estado
lexer.features = {}
lexer.tipo = ""
lexer.buffer = ""   # Vai ter o valor da feature q está a ser reconhecida no momento

# Reading the input
for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer: 
        pass 
print(lexer.features)

