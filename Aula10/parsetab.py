
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "INPUT INT PRINT STR id strProgram : Declarations StatementsDeclarations : Declarations DeclarationDeclarations : Declarations : Type IdListType : INTType : STRIdList : IdList ',' idIdList : idStatements : Statements StatementStatements : StatementStatements : AtribStatement : PRINT '(' PrintArgs ')'PrintArgs : PrintArgs ',' PrintArgPrintArgs : PrintArgPrintArgs : ExpAtrib : id '=' ExpDeclaration : Type IdListDeclaration : PrintArg : idPrintArg : strPrintArg : ExpExp : INT '(' Exp ')'Exp : INPUT '(' str ')'"
    
_lr_action_items = {'PRINT':([0,2,6,7,8,9,13,14,15,16,27,28,29,37,38,],[-3,11,11,-2,-10,-11,-4,-8,-9,-17,-16,-7,-12,-22,-23,]),'id':([0,2,3,4,5,7,10,13,14,16,17,19,28,30,],[-3,12,14,-5,-6,-2,14,-4,-8,-17,23,28,-7,23,]),'INT':([0,2,7,13,14,16,17,18,28,30,31,],[4,4,-2,-4,-8,-17,25,25,-7,25,25,]),'STR':([0,2,7,13,14,16,28,],[5,5,-2,-4,-8,-17,-7,]),'$end':([1,6,8,9,15,27,29,37,38,],[0,-1,-10,-11,-9,-16,-12,-22,-23,]),'(':([11,25,26,],[17,31,32,]),'=':([12,],[18,]),',':([13,14,16,20,21,22,23,24,28,33,34,37,38,],[19,-8,19,30,-14,-15,-19,-20,-7,-13,-21,-22,-23,]),'str':([17,30,32,],[24,24,36,]),'INPUT':([17,18,30,31,],[26,26,26,26,]),')':([20,21,22,23,24,33,34,35,36,37,38,],[29,-14,-15,-19,-20,-13,-21,37,38,-22,-23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'Declarations':([0,],[2,]),'Type':([0,2,],[3,10,]),'Statements':([2,],[6,]),'Declaration':([2,],[7,]),'Statement':([2,6,],[8,15,]),'Atrib':([2,],[9,]),'IdList':([3,10,],[13,16,]),'PrintArgs':([17,],[20,]),'PrintArg':([17,30,],[21,33,]),'Exp':([17,18,30,31,],[22,27,34,35,]),}

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
  ('Atrib -> id = Exp','Atrib',3,'p_Atrib','lp_sin.py',53),
  ('Declaration -> Type IdList','Declaration',2,'p_Declaration','lp_sin.py',56),
  ('Declaration -> <empty>','Declaration',0,'p_Declaration_empty','lp_sin.py',59),
  ('PrintArg -> id','PrintArg',1,'p_PrintArg_id','lp_sin.py',62),
  ('PrintArg -> str','PrintArg',1,'p_PrintArg_str','lp_sin.py',65),
  ('PrintArg -> Exp','PrintArg',1,'p_PrintArg_Exp','lp_sin.py',68),
  ('Exp -> INT ( Exp )','Exp',4,'p_Exp_int','lp_sin.py',71),
  ('Exp -> INPUT ( str )','Exp',4,'p_Exp_input','lp_sin.py',74),
]
