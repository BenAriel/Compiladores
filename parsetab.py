
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALL AND CLASS_IDENTIFIER COMMA Class DATA_TYPE DIVIDE DisjointClasses DisjointWith EQUALS EXACTLY EquivalentTo GREATER_THAN IndividualNames Individuals LEFT_BRACKET LEFT_CURLY_BRACKET LEFT_PAREN LESS_THAN Literal MAX MIN MINUS NAMESPACEID NCName NMTOKEN NOT NUMBER Name ONLY OR PLUS PROPERTY_IDENTIFIER PROPERTY_IDENTIFIER_has PROPERTY_IDENTIFIER_is_Of PlainLiteral RIGHT_BRACKET RIGHT_CURLY_BRACKET RIGHT_PAREN SOME SubClassOf THAT TIMES VALUE XMLLiteral anyURI base64Binary boolean byte dateTime dateTimeStamp decimal double float hexBinary int integer langString languague long negativeInteger nonNegativeInteger owl rational rdf rdfs real string xsdstatements : statement\n                  | statement statementsstatement : Class CLASS_IDENTIFIER SubClassOf primitive_class_mandatory statement_class_disjoin statement_class_individualsstatement_reserved_word : SOME\n                               | EXACTLY\n                               | MIN\n                               | MAX\n                               | OR\n                               | ONLY\n                               | AND\n                               | VALUEstatement_property_identify : PROPERTY_IDENTIFIER_has\n                                   | PROPERTY_IDENTIFIER_is_Of\n                                   | PROPERTY_IDENTIFIERprimitive_class_mandatory : statement_property_identify statement_reserved_word CLASS_IDENTIFIER\n                                 | statement_property_identify statement_reserved_word CLASS_IDENTIFIER COMMA primitive_class_mandatory\n                                 | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE\n                                 | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE COMMA primitive_class_mandatory\n                                 | CLASS_IDENTIFIER\n                                 | CLASS_IDENTIFIER COMMA primitive_class_mandatorystatement_class_disjoin : empty\n                               | DisjointClasses statement_class_disjoin_checkstatement_class_disjoin_check : CLASS_IDENTIFIER\n                                     | CLASS_IDENTIFIER COMMA statement_class_disjoin_checkstatement_class_individuals : empty\n                                   | Individuals statement_class_individuals_checkstatement_class_individuals_check : IndividualNames\n                                         | IndividualNames COMMA statement_class_individuals_checkstatement : Class CLASS_IDENTIFIER EquivalentTo CLASS_IDENTIFIER AND LEFT_PAREN statement_defined_class_equivalent statement_class_disjoin statement_class_individualsstatement_defined_class_equivalent : statement_property_identify statement_reserved_word CLASS_IDENTIFIER RIGHT_PAREN\n    | statement_property_identify statement_reserved_word CLASS_IDENTIFIER RIGHT_PAREN COMMA statement_defined_class_equivalent\n                                          | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET RIGHT_PAREN\n                                          | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET RIGHT_PAREN COMMA statement_defined_class_equivalent statement_operator_symbol : LESS_THAN\n    | GREATER_THAN\n    | EQUALS\n    |  GREATER_THAN EQUALS\n    | LESS_THAN EQUALSstatement : Class CLASS_IDENTIFIER EquivalentTo CLASS_IDENTIFIER AND nested_descriptionsnested_descriptions : nested_descriptions AND nested_descriptions\n                           | nested_descriptions OR nested_descriptions\n                           | LEFT_PAREN nested_descriptions RIGHT_PAREN\n                           | statement_property_identify statement_reserved_word nested_descriptions\n                           | statement_property_identify statement_reserved_word CLASS_IDENTIFIER\n                           | statement_property_identify statement_reserved_word VALUE CLASS_IDENTIFIER\n                           | statement_property_identify statement_reserved_word VALUE IndividualNames\n                           | statement_property_identify statement_reserved_word VALUE nested_descriptions\n                           | statement_property_identify statement_reserved_word ONLY CLASS_IDENTIFIER\n                           | statement_property_identify statement_reserved_word ONLY nested_descriptions\n                           | statement_property_identify statement_reserved_word SOME CLASS_IDENTIFIER\n                           | statement_property_identify statement_reserved_word SOME nested_descriptions\n                           | CLASS_IDENTIFIERstatement : Class CLASS_IDENTIFIER SubClassOf CLASS_IDENTIFIER COMMA closed_axiom_mandatoryclosed_axiom_mandatory : CLASS_IDENTIFIER\n                              | statement_property_restriction\n                              | CLASS_IDENTIFIER COMMA closed_axiom_mandatory\n                              | statement_property_restriction COMMA closed_axiom_mandatorystatement_property_restriction : statement_property_identify SOME CLASS_IDENTIFIER\n                                      | statement_property_identify ONLY LEFT_PAREN closed_axiom_restriction_combination RIGHT_PARENclosed_axiom_restriction_combination : CLASS_IDENTIFIER\n                                            | CLASS_IDENTIFIER OR closed_axiom_restriction_combinationstatement : Class CLASS_IDENTIFIER EquivalentTo LEFT_CURLY_BRACKET statement_enumerated_class_check RIGHT_CURLY_BRACKETstatement_enumerated_class_check : IndividualNames\n                                        | IndividualNames COMMA statement_enumerated_class_checkstatement : Class CLASS_IDENTIFIER EquivalentTo statement_covered_class_checkstatement_covered_class_check : CLASS_IDENTIFIER\n                                     | CLASS_IDENTIFIER OR statement_covered_class_checkempty :'
    
_lr_action_items = {'Class':([0,2,8,9,14,16,18,19,34,35,36,37,39,40,42,43,44,46,48,50,51,52,58,59,62,64,71,72,73,75,78,79,80,82,83,85,86,87,88,97,99,100,103,104,105,106,107,108,109,110,112,118,129,131,],[3,3,-19,-68,-66,-65,-68,-21,-19,-53,-20,-55,-3,-25,-22,-23,-15,-52,-39,-66,-67,-62,-26,-27,-17,-68,-56,-57,-54,-58,-24,-19,-16,-68,-42,-40,-41,-43,-44,-28,-18,-29,-45,-46,-47,-48,-49,-50,-51,-59,-30,-31,-32,-33,]),'$end':([1,2,4,8,9,14,16,18,19,34,35,36,37,39,40,42,43,44,46,48,50,51,52,58,59,62,64,71,72,73,75,78,79,80,82,83,85,86,87,88,97,99,100,103,104,105,106,107,108,109,110,112,118,129,131,],[0,-1,-2,-19,-68,-66,-65,-68,-21,-19,-53,-20,-55,-3,-25,-22,-23,-15,-52,-39,-66,-67,-62,-26,-27,-17,-68,-56,-57,-54,-58,-24,-19,-16,-68,-42,-40,-41,-43,-44,-28,-18,-29,-45,-46,-47,-48,-49,-50,-51,-59,-30,-31,-32,-33,]),'CLASS_IDENTIFIER':([3,6,7,17,20,21,22,23,24,25,26,27,28,29,30,31,47,54,55,56,57,60,61,63,67,68,69,76,81,84,89,90,91,92,93,98,111,123,],[5,8,14,34,43,44,-4,-5,-6,-7,-8,-9,-10,-11,46,50,46,34,73,75,-9,43,79,46,46,46,88,96,79,101,103,106,108,73,75,79,96,127,]),'SubClassOf':([5,],[6,]),'EquivalentTo':([5,],[7,]),'PROPERTY_IDENTIFIER_has':([6,17,22,23,24,25,26,27,28,29,30,47,54,55,61,63,67,68,69,81,84,89,90,91,92,98,115,130,],[11,11,-4,-5,-6,-7,-8,-9,-10,-11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'PROPERTY_IDENTIFIER_is_Of':([6,17,22,23,24,25,26,27,28,29,30,47,54,55,61,63,67,68,69,81,84,89,90,91,92,98,115,130,],[12,12,-4,-5,-6,-7,-8,-9,-10,-11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'PROPERTY_IDENTIFIER':([6,17,22,23,24,25,26,27,28,29,30,47,54,55,61,63,67,68,69,81,84,89,90,91,92,98,115,130,],[13,13,-4,-5,-6,-7,-8,-9,-10,-11,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'LEFT_CURLY_BRACKET':([7,],[15,]),'COMMA':([8,33,34,37,43,44,59,62,73,75,79,110,112,129,],[17,53,54,55,60,61,77,81,92,-58,98,-59,115,130,]),'DisjointClasses':([8,9,34,36,44,62,64,79,80,99,112,118,129,131,],[-19,20,-19,-20,-15,-17,20,-19,-16,-18,-30,-31,-32,-33,]),'Individuals':([8,9,18,19,34,36,42,43,44,62,64,78,79,80,82,99,112,118,129,131,],[-19,-68,41,-21,-19,-20,-22,-23,-15,-17,-68,-24,-19,-16,41,-18,-30,-31,-32,-33,]),'SOME':([10,11,12,13,22,23,24,25,26,27,28,29,38,49,66,69,74,84,117,],[22,-12,-13,-14,-4,-5,-6,-7,-8,-9,-10,-11,56,22,22,91,93,91,22,]),'EXACTLY':([10,11,12,13,38,49,66,117,],[23,-12,-13,-14,23,23,23,23,]),'MIN':([10,11,12,13,38,49,66,117,],[24,-12,-13,-14,24,24,24,24,]),'MAX':([10,11,12,13,38,49,66,117,],[25,-12,-13,-14,25,25,25,25,]),'OR':([10,11,12,13,14,38,46,48,49,50,65,66,83,85,86,87,88,96,101,103,104,105,106,107,108,109,117,],[26,-12,-13,-14,31,26,-52,68,26,31,68,26,-42,68,68,68,-44,111,-44,-45,-46,68,-48,68,-50,68,26,]),'ONLY':([10,11,12,13,22,23,24,25,26,27,28,29,38,49,66,69,74,84,117,],[27,-12,-13,-14,-4,-5,-6,-7,-8,-9,-10,-11,57,27,27,90,94,90,27,]),'AND':([10,11,12,13,14,38,46,48,49,65,66,83,85,86,87,88,101,103,104,105,106,107,108,109,117,],[28,-12,-13,-14,30,28,-52,67,28,67,28,-42,67,67,67,-44,-44,-45,-46,67,-48,67,-50,67,28,]),'VALUE':([10,11,12,13,22,23,24,25,26,27,28,29,38,49,66,69,84,117,],[29,-12,-13,-14,-4,-5,-6,-7,-8,-9,-10,-11,29,29,29,89,89,29,]),'IndividualNames':([15,41,53,77,89,],[33,59,33,59,104,]),'NAMESPACEID':([21,22,23,24,25,26,27,28,29,56,57,84,123,],[45,-4,-5,-6,-7,-8,-9,-10,-11,-4,-9,102,102,]),'LEFT_PAREN':([22,23,24,25,26,27,28,29,30,47,57,63,67,68,69,84,89,90,91,94,],[-4,-5,-6,-7,-8,-9,-10,-11,47,63,76,63,63,63,63,63,63,63,63,76,]),'RIGHT_CURLY_BRACKET':([32,33,70,],[52,-63,-64,]),'DATA_TYPE':([45,102,],[62,113,]),'RIGHT_PAREN':([46,65,83,85,86,87,88,95,96,101,103,104,105,106,107,108,109,114,127,128,],[-52,83,-42,-40,-41,-43,-44,110,-60,112,-45,-46,-47,-48,-49,-50,-51,-61,112,129,]),'LEFT_BRACKET':([113,],[116,]),'LESS_THAN':([116,],[120,]),'GREATER_THAN':([116,],[121,]),'EQUALS':([116,120,121,],[122,125,126,]),'NUMBER':([119,120,121,122,125,126,],[124,-34,-35,-36,-38,-37,]),'RIGHT_BRACKET':([124,],[128,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,2,],[1,4,]),'statement':([0,2,],[2,2,]),'primitive_class_mandatory':([6,17,54,61,81,98,],[9,36,36,80,99,36,]),'statement_property_identify':([6,17,30,47,54,55,61,63,67,68,69,81,84,89,90,91,92,98,115,130,],[10,38,49,66,38,74,10,49,49,49,49,10,49,49,49,49,74,10,117,117,]),'statement_covered_class_check':([7,31,],[16,51,]),'statement_class_disjoin':([9,64,],[18,82,]),'empty':([9,18,64,82,],[19,40,19,40,]),'statement_reserved_word':([10,38,49,66,117,],[21,21,69,84,123,]),'statement_enumerated_class_check':([15,53,],[32,70,]),'closed_axiom_mandatory':([17,54,55,92,],[35,71,72,71,]),'statement_property_restriction':([17,54,55,92,],[37,37,37,37,]),'statement_class_individuals':([18,82,],[39,100,]),'statement_class_disjoin_check':([20,60,],[42,78,]),'nested_descriptions':([30,47,63,67,68,69,84,89,90,91,],[48,65,65,85,86,87,87,105,107,109,]),'statement_class_individuals_check':([41,77,],[58,97,]),'statement_defined_class_equivalent':([47,115,130,],[64,118,131,]),'closed_axiom_restriction_combination':([76,111,],[95,114,]),'statement_operator_symbol':([116,],[119,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statement','statements',1,'p_statements','Sintatico.py',6),
  ('statements -> statement statements','statements',2,'p_statements','Sintatico.py',7),
  ('statement -> Class CLASS_IDENTIFIER SubClassOf primitive_class_mandatory statement_class_disjoin statement_class_individuals','statement',6,'p_statement_primitive_class','Sintatico.py',12),
  ('statement_reserved_word -> SOME','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',16),
  ('statement_reserved_word -> EXACTLY','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',17),
  ('statement_reserved_word -> MIN','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',18),
  ('statement_reserved_word -> MAX','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',19),
  ('statement_reserved_word -> OR','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',20),
  ('statement_reserved_word -> ONLY','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',21),
  ('statement_reserved_word -> AND','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',22),
  ('statement_reserved_word -> VALUE','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',23),
  ('statement_property_identify -> PROPERTY_IDENTIFIER_has','statement_property_identify',1,'p_statement_property_identify','Sintatico.py',27),
  ('statement_property_identify -> PROPERTY_IDENTIFIER_is_Of','statement_property_identify',1,'p_statement_property_identify','Sintatico.py',28),
  ('statement_property_identify -> PROPERTY_IDENTIFIER','statement_property_identify',1,'p_statement_property_identify','Sintatico.py',29),
  ('primitive_class_mandatory -> statement_property_identify statement_reserved_word CLASS_IDENTIFIER','primitive_class_mandatory',3,'p_primitive_class_mandatory','Sintatico.py',33),
  ('primitive_class_mandatory -> statement_property_identify statement_reserved_word CLASS_IDENTIFIER COMMA primitive_class_mandatory','primitive_class_mandatory',5,'p_primitive_class_mandatory','Sintatico.py',34),
  ('primitive_class_mandatory -> statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE','primitive_class_mandatory',4,'p_primitive_class_mandatory','Sintatico.py',35),
  ('primitive_class_mandatory -> statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE COMMA primitive_class_mandatory','primitive_class_mandatory',6,'p_primitive_class_mandatory','Sintatico.py',36),
  ('primitive_class_mandatory -> CLASS_IDENTIFIER','primitive_class_mandatory',1,'p_primitive_class_mandatory','Sintatico.py',37),
  ('primitive_class_mandatory -> CLASS_IDENTIFIER COMMA primitive_class_mandatory','primitive_class_mandatory',3,'p_primitive_class_mandatory','Sintatico.py',38),
  ('statement_class_disjoin -> empty','statement_class_disjoin',1,'p_statement_class_disjoin','Sintatico.py',42),
  ('statement_class_disjoin -> DisjointClasses statement_class_disjoin_check','statement_class_disjoin',2,'p_statement_class_disjoin','Sintatico.py',43),
  ('statement_class_disjoin_check -> CLASS_IDENTIFIER','statement_class_disjoin_check',1,'p_statement_class_disjoin_check','Sintatico.py',47),
  ('statement_class_disjoin_check -> CLASS_IDENTIFIER COMMA statement_class_disjoin_check','statement_class_disjoin_check',3,'p_statement_class_disjoin_check','Sintatico.py',48),
  ('statement_class_individuals -> empty','statement_class_individuals',1,'p_statement_class_individuals','Sintatico.py',52),
  ('statement_class_individuals -> Individuals statement_class_individuals_check','statement_class_individuals',2,'p_statement_class_individuals','Sintatico.py',53),
  ('statement_class_individuals_check -> IndividualNames','statement_class_individuals_check',1,'p_statement_class_individuals_check','Sintatico.py',57),
  ('statement_class_individuals_check -> IndividualNames COMMA statement_class_individuals_check','statement_class_individuals_check',3,'p_statement_class_individuals_check','Sintatico.py',58),
  ('statement -> Class CLASS_IDENTIFIER EquivalentTo CLASS_IDENTIFIER AND LEFT_PAREN statement_defined_class_equivalent statement_class_disjoin statement_class_individuals','statement',9,'p_statement_defined_class','Sintatico.py',64),
  ('statement_defined_class_equivalent -> statement_property_identify statement_reserved_word CLASS_IDENTIFIER RIGHT_PAREN','statement_defined_class_equivalent',4,'p_statement_defined_class_equivalent','Sintatico.py',68),
  ('statement_defined_class_equivalent -> statement_property_identify statement_reserved_word CLASS_IDENTIFIER RIGHT_PAREN COMMA statement_defined_class_equivalent','statement_defined_class_equivalent',6,'p_statement_defined_class_equivalent','Sintatico.py',69),
  ('statement_defined_class_equivalent -> statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET RIGHT_PAREN','statement_defined_class_equivalent',9,'p_statement_defined_class_equivalent','Sintatico.py',70),
  ('statement_defined_class_equivalent -> statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET RIGHT_PAREN COMMA statement_defined_class_equivalent','statement_defined_class_equivalent',11,'p_statement_defined_class_equivalent','Sintatico.py',71),
  ('statement_operator_symbol -> LESS_THAN','statement_operator_symbol',1,'p_statement_operator_symbol','Sintatico.py',75),
  ('statement_operator_symbol -> GREATER_THAN','statement_operator_symbol',1,'p_statement_operator_symbol','Sintatico.py',76),
  ('statement_operator_symbol -> EQUALS','statement_operator_symbol',1,'p_statement_operator_symbol','Sintatico.py',77),
  ('statement_operator_symbol -> GREATER_THAN EQUALS','statement_operator_symbol',2,'p_statement_operator_symbol','Sintatico.py',78),
  ('statement_operator_symbol -> LESS_THAN EQUALS','statement_operator_symbol',2,'p_statement_operator_symbol','Sintatico.py',79),
  ('statement -> Class CLASS_IDENTIFIER EquivalentTo CLASS_IDENTIFIER AND nested_descriptions','statement',6,'p_statement_aninhada_class','Sintatico.py',84),
  ('nested_descriptions -> nested_descriptions AND nested_descriptions','nested_descriptions',3,'p_nested_descriptions','Sintatico.py',88),
  ('nested_descriptions -> nested_descriptions OR nested_descriptions','nested_descriptions',3,'p_nested_descriptions','Sintatico.py',89),
  ('nested_descriptions -> LEFT_PAREN nested_descriptions RIGHT_PAREN','nested_descriptions',3,'p_nested_descriptions','Sintatico.py',90),
  ('nested_descriptions -> statement_property_identify statement_reserved_word nested_descriptions','nested_descriptions',3,'p_nested_descriptions','Sintatico.py',91),
  ('nested_descriptions -> statement_property_identify statement_reserved_word CLASS_IDENTIFIER','nested_descriptions',3,'p_nested_descriptions','Sintatico.py',92),
  ('nested_descriptions -> statement_property_identify statement_reserved_word VALUE CLASS_IDENTIFIER','nested_descriptions',4,'p_nested_descriptions','Sintatico.py',93),
  ('nested_descriptions -> statement_property_identify statement_reserved_word VALUE IndividualNames','nested_descriptions',4,'p_nested_descriptions','Sintatico.py',94),
  ('nested_descriptions -> statement_property_identify statement_reserved_word VALUE nested_descriptions','nested_descriptions',4,'p_nested_descriptions','Sintatico.py',95),
  ('nested_descriptions -> statement_property_identify statement_reserved_word ONLY CLASS_IDENTIFIER','nested_descriptions',4,'p_nested_descriptions','Sintatico.py',96),
  ('nested_descriptions -> statement_property_identify statement_reserved_word ONLY nested_descriptions','nested_descriptions',4,'p_nested_descriptions','Sintatico.py',97),
  ('nested_descriptions -> statement_property_identify statement_reserved_word SOME CLASS_IDENTIFIER','nested_descriptions',4,'p_nested_descriptions','Sintatico.py',98),
  ('nested_descriptions -> statement_property_identify statement_reserved_word SOME nested_descriptions','nested_descriptions',4,'p_nested_descriptions','Sintatico.py',99),
  ('nested_descriptions -> CLASS_IDENTIFIER','nested_descriptions',1,'p_nested_descriptions','Sintatico.py',100),
  ('statement -> Class CLASS_IDENTIFIER SubClassOf CLASS_IDENTIFIER COMMA closed_axiom_mandatory','statement',6,'p_statement_closed_axiom_class','Sintatico.py',113),
  ('closed_axiom_mandatory -> CLASS_IDENTIFIER','closed_axiom_mandatory',1,'p_closed_axiom_mandatory','Sintatico.py',117),
  ('closed_axiom_mandatory -> statement_property_restriction','closed_axiom_mandatory',1,'p_closed_axiom_mandatory','Sintatico.py',118),
  ('closed_axiom_mandatory -> CLASS_IDENTIFIER COMMA closed_axiom_mandatory','closed_axiom_mandatory',3,'p_closed_axiom_mandatory','Sintatico.py',119),
  ('closed_axiom_mandatory -> statement_property_restriction COMMA closed_axiom_mandatory','closed_axiom_mandatory',3,'p_closed_axiom_mandatory','Sintatico.py',120),
  ('statement_property_restriction -> statement_property_identify SOME CLASS_IDENTIFIER','statement_property_restriction',3,'p_statement_property_restriction','Sintatico.py',124),
  ('statement_property_restriction -> statement_property_identify ONLY LEFT_PAREN closed_axiom_restriction_combination RIGHT_PAREN','statement_property_restriction',5,'p_statement_property_restriction','Sintatico.py',125),
  ('closed_axiom_restriction_combination -> CLASS_IDENTIFIER','closed_axiom_restriction_combination',1,'p_closed_axiom_restriction_combination','Sintatico.py',129),
  ('closed_axiom_restriction_combination -> CLASS_IDENTIFIER OR closed_axiom_restriction_combination','closed_axiom_restriction_combination',3,'p_closed_axiom_restriction_combination','Sintatico.py',130),
  ('statement -> Class CLASS_IDENTIFIER EquivalentTo LEFT_CURLY_BRACKET statement_enumerated_class_check RIGHT_CURLY_BRACKET','statement',6,'p_statement_enumerated_class','Sintatico.py',135),
  ('statement_enumerated_class_check -> IndividualNames','statement_enumerated_class_check',1,'p_statement_enumerated_class_check','Sintatico.py',139),
  ('statement_enumerated_class_check -> IndividualNames COMMA statement_enumerated_class_check','statement_enumerated_class_check',3,'p_statement_enumerated_class_check','Sintatico.py',140),
  ('statement -> Class CLASS_IDENTIFIER EquivalentTo statement_covered_class_check','statement',4,'p_statement_covered_class','Sintatico.py',145),
  ('statement_covered_class_check -> CLASS_IDENTIFIER','statement_covered_class_check',1,'p_statement_covered_class_check','Sintatico.py',149),
  ('statement_covered_class_check -> CLASS_IDENTIFIER OR statement_covered_class_check','statement_covered_class_check',3,'p_statement_covered_class_check','Sintatico.py',150),
  ('empty -> <empty>','empty',0,'p_empty','Sintatico.py',155),
]
