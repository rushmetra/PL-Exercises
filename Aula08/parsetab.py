
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMAIMENleftMULDIVDIV MAI MEN MUL NUMFrase       : ElementosElementos   : Elementos MAI ElementosElementos   : Elementos MEN ElementosElementos   : Elementos MUL ElementosElementos   : Elementos DIV ElementosElementos  : ExpressaoExpressao  : NUM'
    
_lr_action_items = {'NUM':([0,5,6,7,8,],[4,4,4,4,4,]),'$end':([1,2,3,4,9,10,11,12,],[0,-1,-6,-7,-2,-3,-4,-5,]),'MAI':([2,3,4,9,10,11,12,],[5,-6,-7,-2,-3,-4,-5,]),'MEN':([2,3,4,9,10,11,12,],[6,-6,-7,-2,-3,-4,-5,]),'MUL':([2,3,4,9,10,11,12,],[7,-6,-7,7,7,-4,-5,]),'DIV':([2,3,4,9,10,11,12,],[8,-6,-7,8,8,-4,-5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Frase':([0,],[1,]),'Elementos':([0,5,6,7,8,],[2,9,10,11,12,]),'Expressao':([0,5,6,7,8,],[3,3,3,3,3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Frase","S'",1,None,None,None),
  ('Frase -> Elementos','Frase',1,'p_frase','precedence_yacc.py',21),
  ('Elementos -> Elementos MAI Elementos','Elementos',3,'p_elementos_mais','precedence_yacc.py',25),
  ('Elementos -> Elementos MEN Elementos','Elementos',3,'p_elementos_menos','precedence_yacc.py',30),
  ('Elementos -> Elementos MUL Elementos','Elementos',3,'p_elementos_vezes','precedence_yacc.py',35),
  ('Elementos -> Elementos DIV Elementos','Elementos',3,'p_elementos_divisao','precedence_yacc.py',40),
  ('Elementos -> Expressao','Elementos',1,'p_elementos_expressao','precedence_yacc.py',45),
  ('Expressao -> NUM','Expressao',1,'p_expressao','precedence_yacc.py',49),
]