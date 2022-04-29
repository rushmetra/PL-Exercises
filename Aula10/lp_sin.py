import ply.yacc as yacc 
from lp_lex import tokens, literals

def p_Program(p):
    "Program : Declarations Statements"

def p_Declarations_list(p):
    "Declarations : Declarations Declaration"

def p_Declarations_empty(p):
    "Declarations : "

def p_Declarations(p):
    "Declarations : Type IdList"

def p_Type_int(p):
    'Type : INT'

def p_Type_str(p):
    'Type : STR' 

def p_IdList_list(p):
    "IdList : IdList ',' id" 

def p_IdList_single(p):
    "IdList : id"     

def p_Statements_list(p):
    "Statements : Statements Statement"

def p_Statements_single(p):
    "Statements : Statement"

def p_Statements_atrib(p):
    "Statements : Atrib"

def p_Statement_print(p):
    "Statement : PRINT '(' PrintArgs ')'"

def p_PrintArgs_list(p):
    "PrintArgs : PrintArgs ',' PrintArg"

def p_PrintArgs_single(p):
    "PrintArgs : PrintArg" 

def p_PrintArgs_exp(p):
    "PrintArgs : Exp" 

def p_Atrib(p):
    "Atrib : id '=' Exp"

def p_Declaration(p):
    "Declaration : Type IdList"

def p_Declaration_empty(p):
    "Declaration : "

def p_PrintArg_id(p):
    "PrintArg : id"

def p_PrintArg_str(p):
    "PrintArg : str"

def p_PrintArg_Exp(p):
    "PrintArg : Exp"

def p_Exp_int(p):
    "Exp : INT '(' Exp ')'"

def p_Exp_input(p):
    "Exp : INPUT '(' str ')'"    

def p_Statement_if(p):
    "Statement : IF '(' Cond ')' CondStatements Else"

def p_Else_empty(p):
    "Else : "

def p_Else(p):
    "Else : ELSE CondStatements"

def p_CondStatements_simple(p):
    "CondStatements : Statement"

def p_CondStatements_compound(p):
    "CondStatements : '{' Statements '}'"

def p_Cond_long(p):
    "Cond : Cond OR Cond2"

def p_Cond(p):
    "Cond : Cond2"

def p_Cond_and(p):
    "Cond : Cond2 AND Cond3"

def p_Cond2(p):
    "Cond2 : Cond3"

def p_Cond3_not(p):
    "Cond3 : NOT ExpRel"

def p_Cond3(p):
    "Cond3 : ExpRel"

def p_ExpRel_gt(p):
    "ExpRel : Exp '>' Exp"

def p_ExpRel_lt(p):
    "ExpRel : Exp '<' Exp"

def p_ExpRel_ge(p):
    "ExpRel : Exp GE Exp"

def p_ExpRel_le(p):
    "ExpRel : Exp LE Exp"

def p_ExpRel_eq(p):
    "ExpRel : Exp EQ Exp"

def p_ExpRel_neq(p):
    "ExpRel : Exp NEQ Exp"


def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False



# Build the parser
parser = yacc.yacc()

# Read line from input and parse it
import sys
parser.success = True
program = sys.stdin.read()
parser.parse(program)
if parser.success:
    print("Programa estruturalmente correto!")
else:
    print("Programa com erros... Corrija e tente novamente!")