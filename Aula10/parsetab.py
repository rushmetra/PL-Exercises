
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND COMMENT ELSE EQ GE IF INPUT INT LE NEQ NOT OR PRINT STR id strProgram : Declarations StatementsDeclarations : Declarations DeclarationDeclarations : Declarations : Type IdListType : INTType : STRIdList : IdList ',' idIdList : idStatements : Statements StatementStatements : StatementStatements : AtribStatement : PRINT '(' PrintArgs ')'PrintArgs : PrintArgs ',' PrintArgPrintArgs : PrintArgPrintArgs : ExpAtrib : id '=' ExpDeclaration : Type IdListDeclaration : Exp : idPrintArg : strPrintArg : ExpExp : INT '(' Exp ')'Exp : INPUT '(' str ')'Statement : IF '(' Cond ')' CondStatements ElseElse : Else : ELSE CondStatementsCondStatements : StatementCondStatements : '{' Statements '}'Cond : Cond OR Cond2Cond : Cond2Cond : Cond2 AND Cond3Cond2 : Cond3Cond3 : NOT ExpRelCond3 : ExpRelExpRel : Exp '>' ExpExpRel : Exp '<' ExpExpRel : Exp GE ExpExpRel : Exp LE ExpExpRel : Exp EQ ExpExpRel : Exp NEQ Exp"
    
_lr_action_items = {'PRINT':([0,2,6,7,8,9,14,15,16,17,26,35,36,37,41,55,56,57,66,67,68,69,70,71,72,],[-3,11,11,-2,-10,-11,-4,-8,-9,-17,-19,-16,-7,-12,11,-25,-27,11,-22,-23,-24,11,11,-26,-28,]),'IF':([0,2,6,7,8,9,14,15,16,17,26,35,36,37,41,55,56,57,66,67,68,69,70,71,72,],[-3,12,12,-2,-10,-11,-4,-8,-9,-17,-19,-16,-7,-12,12,-25,-27,12,-22,-23,-24,12,12,-26,-28,]),'id':([0,2,3,4,5,7,10,14,15,17,18,19,20,21,32,36,38,39,42,43,45,46,47,48,49,50,57,],[-3,13,15,-5,-6,-2,15,-4,-8,-17,26,26,26,36,26,-7,26,26,26,26,26,26,26,26,26,26,13,]),'INT':([0,2,7,14,15,17,18,19,20,32,36,38,39,42,43,45,46,47,48,49,50,],[4,4,-2,-4,-8,-17,27,27,27,27,-7,27,27,27,27,27,27,27,27,27,27,]),'STR':([0,2,7,14,15,17,36,],[5,5,-2,-4,-8,-17,-7,]),'$end':([1,6,8,9,16,26,35,37,55,56,66,67,68,71,72,],[0,-1,-10,-11,-9,-19,-16,-12,-25,-27,-22,-23,-24,-26,-28,]),'}':([8,9,16,26,35,37,55,56,66,67,68,70,71,72,],[-10,-11,-9,-19,-16,-12,-25,-27,-22,-23,-24,72,-26,-28,]),'(':([11,12,27,28,],[18,19,39,40,]),'=':([13,],[20,]),',':([14,15,17,22,23,24,25,26,36,51,52,66,67,],[21,-8,21,38,-14,-15,-20,-19,-7,-13,-21,-22,-23,]),'str':([18,38,40,],[25,25,54,]),'INPUT':([18,19,20,32,38,39,42,43,45,46,47,48,49,50,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'NOT':([19,42,43,],[32,32,32,]),')':([22,23,24,25,26,29,30,31,33,44,51,52,53,54,58,59,60,61,62,63,64,65,66,67,],[37,-14,-15,-20,-19,41,-30,-32,-34,-33,-13,-21,66,67,-29,-31,-35,-36,-37,-38,-39,-40,-22,-23,]),'>':([26,34,66,67,],[-19,45,-22,-23,]),'<':([26,34,66,67,],[-19,46,-22,-23,]),'GE':([26,34,66,67,],[-19,47,-22,-23,]),'LE':([26,34,66,67,],[-19,48,-22,-23,]),'EQ':([26,34,66,67,],[-19,49,-22,-23,]),'NEQ':([26,34,66,67,],[-19,50,-22,-23,]),'AND':([26,30,31,33,44,60,61,62,63,64,65,66,67,],[-19,43,-32,-34,-33,-35,-36,-37,-38,-39,-40,-22,-23,]),'OR':([26,29,30,31,33,44,58,59,60,61,62,63,64,65,66,67,],[-19,42,-30,-32,-34,-33,-29,-31,-35,-36,-37,-38,-39,-40,-22,-23,]),'ELSE':([37,55,56,68,71,72,],[-12,69,-27,-24,-26,-28,]),'{':([41,69,],[57,57,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'Declarations':([0,],[2,]),'Type':([0,2,],[3,10,]),'Statements':([2,57,],[6,70,]),'Declaration':([2,],[7,]),'Statement':([2,6,41,57,69,70,],[8,16,56,8,56,16,]),'Atrib':([2,57,],[9,9,]),'IdList':([3,10,],[14,17,]),'PrintArgs':([18,],[22,]),'PrintArg':([18,38,],[23,51,]),'Exp':([18,19,20,32,38,39,42,43,45,46,47,48,49,50,],[24,34,35,34,52,53,34,34,60,61,62,63,64,65,]),'Cond':([19,],[29,]),'Cond2':([19,42,],[30,58,]),'Cond3':([19,42,43,],[31,31,59,]),'ExpRel':([19,32,42,43,],[33,44,33,33,]),'CondStatements':([41,69,],[55,71,]),'Else':([55,],[68,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Program","S'",1,None,None,None),
  ('Program -> Declarations Statements','Program',2,'p_Program','lp_sin.py',5),
  ('Declarations -> Declarations Declaration','Declarations',2,'p_Declarations_list','lp_sin.py',8),
  ('Declarations -> <empty>','Declarations',0,'p_Declarations_empty','lp_sin.py',11),
  ('Declarations -> Type IdList','Declarations',2,'p_Declarations','lp_sin.py',14),
  ('Type -> INT','Type',1,'p_Type_int','lp_sin.py',17),
  ('Type -> STR','Type',1,'p_Type_str','lp_sin.py',20),
  ('IdList -> IdList , id','IdList',3,'p_IdList_list','lp_sin.py',23),
  ('IdList -> id','IdList',1,'p_IdList_single','lp_sin.py',26),
  ('Statements -> Statements Statement','Statements',2,'p_Statements_list','lp_sin.py',29),
  ('Statements -> Statement','Statements',1,'p_Statements_single','lp_sin.py',32),
  ('Statements -> Atrib','Statements',1,'p_Statements_atrib','lp_sin.py',35),
  ('Statement -> PRINT ( PrintArgs )','Statement',4,'p_Statement_print','lp_sin.py',38),
  ('PrintArgs -> PrintArgs , PrintArg','PrintArgs',3,'p_PrintArgs_list','lp_sin.py',41),
  ('PrintArgs -> PrintArg','PrintArgs',1,'p_PrintArgs_single','lp_sin.py',44),
  ('PrintArgs -> Exp','PrintArgs',1,'p_PrintArgs_exp','lp_sin.py',47),
  ('Atrib -> id = Exp','Atrib',3,'p_Atrib','lp_sin.py',50),
  ('Declaration -> Type IdList','Declaration',2,'p_Declaration','lp_sin.py',53),
  ('Declaration -> <empty>','Declaration',0,'p_Declaration_empty','lp_sin.py',56),
  ('Exp -> id','Exp',1,'p_Exp_id','lp_sin.py',59),
  ('PrintArg -> str','PrintArg',1,'p_PrintArg_str','lp_sin.py',62),
  ('PrintArg -> Exp','PrintArg',1,'p_PrintArg_Exp','lp_sin.py',65),
  ('Exp -> INT ( Exp )','Exp',4,'p_Exp_int','lp_sin.py',68),
  ('Exp -> INPUT ( str )','Exp',4,'p_Exp_input','lp_sin.py',71),
  ('Statement -> IF ( Cond ) CondStatements Else','Statement',6,'p_Statement_if','lp_sin.py',74),
  ('Else -> <empty>','Else',0,'p_Else_empty','lp_sin.py',77),
  ('Else -> ELSE CondStatements','Else',2,'p_Else','lp_sin.py',80),
  ('CondStatements -> Statement','CondStatements',1,'p_CondStatements_simple','lp_sin.py',83),
  ('CondStatements -> { Statements }','CondStatements',3,'p_CondStatements_compound','lp_sin.py',86),
  ('Cond -> Cond OR Cond2','Cond',3,'p_Cond_long','lp_sin.py',89),
  ('Cond -> Cond2','Cond',1,'p_Cond','lp_sin.py',92),
  ('Cond -> Cond2 AND Cond3','Cond',3,'p_Cond_and','lp_sin.py',95),
  ('Cond2 -> Cond3','Cond2',1,'p_Cond2','lp_sin.py',98),
  ('Cond3 -> NOT ExpRel','Cond3',2,'p_Cond3_not','lp_sin.py',101),
  ('Cond3 -> ExpRel','Cond3',1,'p_Cond3','lp_sin.py',104),
  ('ExpRel -> Exp > Exp','ExpRel',3,'p_ExpRel_gt','lp_sin.py',107),
  ('ExpRel -> Exp < Exp','ExpRel',3,'p_ExpRel_lt','lp_sin.py',110),
  ('ExpRel -> Exp GE Exp','ExpRel',3,'p_ExpRel_ge','lp_sin.py',113),
  ('ExpRel -> Exp LE Exp','ExpRel',3,'p_ExpRel_le','lp_sin.py',116),
  ('ExpRel -> Exp EQ Exp','ExpRel',3,'p_ExpRel_eq','lp_sin.py',119),
  ('ExpRel -> Exp NEQ Exp','ExpRel',3,'p_ExpRel_neq','lp_sin.py',122),
]
