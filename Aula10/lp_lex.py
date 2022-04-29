from re import T
import ply.lex as lex

# cat prog-1.txt | python3.9 lp_sin.py
# cat prog-2.txt | python3.9 lp_sin.py

literals = [',','=','(',')','{','}','<','>']
tokens = ['COMMENT','INT','STR','INPUT','PRINT','IF','ELSE','OR','AND','NOT','GE','LE','EQ','NEQ','id','str']

def t_COMMENT(p):
    r'\#.*'

def t_INT(t):
    r'int'
    return t 

def t_INPUT(t):
    r'input'
    return t 

def t_STR(t):
    r'str'
    return t 

def t_PRINT(t):
    r'print'
    return t 

def t_ELSE(t):
    r'else'
    return t 

def t_IF(t):
    r'if'
    return t 

def t_AND(t):
    r'and'
    return t 

def t_OR(t):
    r'or'
    return t 

def t_NOT(t):
    r'not'
    return t 

def t_GE(t):
    r'>='
    return t 

def t_LE(t):
    r'>='
    return t 

def t_EQ(t):
    r'=='
    return t 

def t_NEQ(t):
    r'!='
    return t 

def t_str(t):
    r'\"[^"]*\"'
    return t 

def t_id(t):
    r'[_a-zA-Z]\w*'
    return t

t_ignore = " \t\n"

def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()