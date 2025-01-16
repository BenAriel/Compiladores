
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALL AND CLASS_IDENTIFIER COMMA Class DATA_TYPE DIVIDE DisjointClasses DisjointWith EQUALS EXACTLY EquivalentTo GREATER_THAN IndividualNames Individuals LEFT_BRACKET LEFT_CURLY_BRACKET LEFT_PAREN LESS_THAN Literal MAX MIN MINUS NAMESPACEID NCName NMTOKEN NOT NUMBER Name ONLY OR PLUS PROPERTY_IDENTIFIER PROPERTY_IDENTIFIER_has PROPERTY_IDENTIFIER_is_Of PlainLiteral RIGHT_BRACKET RIGHT_CURLY_BRACKET RIGHT_PAREN SOME SubClassOf THAT TIMES VALUE XMLLiteral anyURI base64Binary boolean byte dateTime dateTimeStamp decimal double float hexBinary int integer langString languague long negativeInteger nonNegativeInteger owl rational rdf rdfs real string xsdstatements : Class CLASS_IDENTIFIER statement_defined_class statements\n                  | Class CLASS_IDENTIFIER statement_defined_class\n                  | Class CLASS_IDENTIFIER statement_primitive_class\n                  | Class CLASS_IDENTIFIER statement_primitive_class statements\n                  | emptystatement_defined_class : EquivalentTo_possible maybe_suclassof statement_class_disjoin statement_class_individuals\n                               | subclassof_possible EquivalentTo_possible statement_class_disjoin statement_class_individualsstatement_primitive_class : subclassof_possible statement_class_disjoin statement_class_individualsEquivalentTo_possible : EquivalentTo JustDefined\n                             | EquivalentTo nested\n                             | EquivalentTo statement_closed_axiom_class\n                             | EquivalentTo statement_enumerated_class\n                             | EquivalentTo statement_covered_classmaybe_suclassof : subclassof_possible\n                       | emptysubclassof_possible : SubClassOf primitive_class_mandatory\n                           | SubClassOf statement_closed_axiom_classJustDefined :  CLASS_IDENTIFIER AND LEFT_PAREN statement_defined_class_equivalent statement_class_individuals\n                        | CLASS_IDENTIFIER COMMA statement_defined_class_equivalent statement_class_individualsstatement_reserved_word : SOME\n                               | EXACTLY\n                               | MIN\n                               | MAX\n                               | OR\n                               | ONLY\n                               | AND\n                               | VALUEstatement_property_identify : PROPERTY_IDENTIFIER_has\n                                   | PROPERTY_IDENTIFIER_is_Of\n                                   | PROPERTY_IDENTIFIERprimitive_class_mandatory : statement_property_identify statement_reserved_word CLASS_IDENTIFIER\n                                 | statement_property_identify statement_reserved_word CLASS_IDENTIFIER COMMA primitive_class_mandatory\n                                 | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE\n                                 | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE COMMA primitive_class_mandatory\n                                 | CLASS_IDENTIFIER\n                                 | CLASS_IDENTIFIER COMMA primitive_class_mandatorystatement_class_disjoin : empty\n                               | DisjointClasses statement_class_disjoin_checkstatement_class_disjoin_check : CLASS_IDENTIFIER\n                                     | CLASS_IDENTIFIER COMMA statement_class_disjoin_checkstatement_class_individuals : empty\n                                   | Individuals statement_class_individuals_checkstatement_class_individuals_check : IndividualNames\n                                         | IndividualNames COMMA statement_class_individuals_checkstatement_defined_class_equivalent : statement_property_identify statement_reserved_word CLASS_IDENTIFIER RIGHT_PAREN\n    | statement_property_identify statement_reserved_word CLASS_IDENTIFIER RIGHT_PAREN COMMA statement_defined_class_equivalent\n                                          | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET RIGHT_PAREN\n                                          | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET RIGHT_PAREN COMMA statement_defined_class_equivalent statement_operator_symbol : LESS_THAN\n    | GREATER_THAN\n    | EQUALS\n    |  GREATER_THAN EQUALS\n    | LESS_THAN EQUALSnested : nested AND nested\n                           | nested OR nested\n                           | LEFT_PAREN nested RIGHT_PAREN\n                           | statement_property_identify statement_reserved_word nested\n                           | statement_property_identify statement_reserved_word CLASS_IDENTIFIER\n                           | statement_property_identify statement_reserved_word VALUE CLASS_IDENTIFIER\n                           | statement_property_identify statement_reserved_word VALUE nested\n                           | statement_property_identify statement_reserved_word ONLY CLASS_IDENTIFIER\n                           | statement_property_identify statement_reserved_word ONLY nested\n                           | statement_property_identify statement_reserved_word SOME CLASS_IDENTIFIER\n                           | statement_property_identify statement_reserved_word SOME nested\n                           | CLASS_IDENTIFIERstatement_closed_axiom_class : CLASS_IDENTIFIER COMMA closed_axiom_mandatoryclosed_axiom_mandatory : CLASS_IDENTIFIER\n                              | statement_property_restriction\n                              | CLASS_IDENTIFIER COMMA closed_axiom_mandatory\n                              | statement_property_restriction COMMA closed_axiom_mandatorystatement_property_restriction : statement_property_identify SOME CLASS_IDENTIFIER\n                                      | statement_property_identify ONLY LEFT_PAREN closed_axiom_restriction_combination RIGHT_PARENclosed_axiom_restriction_combination : CLASS_IDENTIFIER\n                                            | CLASS_IDENTIFIER OR closed_axiom_restriction_combinationstatement_enumerated_class : LEFT_CURLY_BRACKET statement_enumerated_class_check RIGHT_CURLY_BRACKETstatement_enumerated_class_check : IndividualNames\n                                        | IndividualNames COMMA statement_enumerated_class_checkstatement_covered_class : statement_covered_class_checkstatement_covered_class_check : CLASS_IDENTIFIER\n                                     | CLASS_IDENTIFIER OR statement_covered_class_checkempty :'
    
_lr_action_items = {'Class':([0,5,6,7,8,13,14,15,16,17,18,20,21,22,23,24,25,29,33,34,36,37,38,39,40,42,43,50,64,65,66,67,69,70,72,73,74,76,77,78,79,80,81,85,87,89,90,93,94,97,102,103,104,105,106,107,110,112,113,114,118,120,121,122,126,131,134,136,146,148,],[2,2,2,-81,-81,-81,-14,-15,-81,-81,-37,-9,-10,-11,-12,-13,-65,-78,-16,-17,-35,-81,-81,-8,-41,-38,-39,-65,-6,-7,-42,-43,-54,-55,-67,-81,-66,-68,-79,-80,-56,-57,-58,-75,-31,-35,-36,-40,-81,-19,-59,-60,-61,-62,-63,-64,-33,-44,-18,-69,-71,-70,-35,-32,-45,-34,-72,-46,-47,-48,]),'$end':([0,1,3,5,6,7,8,11,12,13,14,15,16,17,18,20,21,22,23,24,25,29,33,34,36,37,38,39,40,42,43,50,64,65,66,67,69,70,72,73,74,76,77,78,79,80,81,85,87,89,90,93,94,97,102,103,104,105,106,107,110,112,113,114,118,120,121,122,126,131,134,136,146,148,],[-81,0,-5,-2,-3,-81,-81,-1,-4,-81,-14,-15,-81,-81,-37,-9,-10,-11,-12,-13,-65,-78,-16,-17,-35,-81,-81,-8,-41,-38,-39,-65,-6,-7,-42,-43,-54,-55,-67,-81,-66,-68,-79,-80,-56,-57,-58,-75,-31,-35,-36,-40,-81,-19,-59,-60,-61,-62,-63,-64,-33,-44,-18,-69,-71,-70,-35,-32,-45,-34,-72,-46,-47,-48,]),'CLASS_IDENTIFIER':([2,9,10,19,26,44,45,47,48,51,52,53,54,55,56,57,58,59,62,63,68,82,83,84,96,98,99,100,101,109,111,119,123,124,130,135,],[4,25,36,43,50,50,50,72,77,81,-27,-25,-20,-21,-22,-23,-24,-26,87,89,43,102,104,106,72,116,118,-25,72,121,89,129,121,118,121,129,]),'EquivalentTo':([4,8,33,34,36,72,74,76,87,89,90,110,114,118,120,121,122,131,134,],[9,9,-16,-17,-35,-67,-66,-68,-31,-35,-36,-33,-69,-71,-70,-35,-32,-34,-72,]),'SubClassOf':([4,7,20,21,22,23,24,25,29,40,50,66,67,69,70,72,73,74,76,77,78,79,80,81,85,94,97,102,103,104,105,106,107,112,113,114,118,120,126,134,136,146,148,],[10,10,-9,-10,-11,-12,-13,-65,-78,-41,-65,-42,-43,-54,-55,-67,-81,-66,-68,-79,-80,-56,-57,-58,-75,-81,-19,-59,-60,-61,-62,-63,-64,-44,-18,-69,-71,-70,-45,-72,-46,-47,-48,]),'DisjointClasses':([7,8,13,14,15,16,20,21,22,23,24,25,29,33,34,36,40,50,66,67,69,70,72,73,74,76,77,78,79,80,81,85,87,89,90,94,97,102,103,104,105,106,107,110,112,113,114,118,120,121,122,126,131,134,136,146,148,],[-81,19,19,-14,-15,19,-9,-10,-11,-12,-13,-65,-78,-16,-17,-35,-41,-65,-42,-43,-54,-55,-67,-81,-66,-68,-79,-80,-56,-57,-58,-75,-31,-35,-36,-81,-19,-59,-60,-61,-62,-63,-64,-33,-44,-18,-69,-71,-70,-35,-32,-45,-34,-72,-46,-47,-48,]),'Individuals':([7,8,13,14,15,16,17,18,20,21,22,23,24,25,29,33,34,36,37,38,40,42,43,50,66,67,69,70,72,73,74,76,77,78,79,80,81,85,87,89,90,93,94,97,102,103,104,105,106,107,110,112,113,114,118,120,121,122,126,131,134,136,146,148,],[-81,-81,-81,-14,-15,-81,41,-37,-9,-10,-11,-12,-13,-65,-78,-16,-17,-35,41,41,-41,-38,-39,-65,-42,-43,-54,-55,-67,41,-66,-68,-79,-80,-56,-57,-58,-75,-31,-35,-36,-40,41,-19,-59,-60,-61,-62,-63,-64,-33,-44,-18,-69,-71,-70,-35,-32,-45,-34,-72,-46,-47,-48,]),'LEFT_PAREN':([9,26,44,45,46,51,52,53,54,55,56,57,58,59,82,83,84,100,125,],[26,26,26,26,71,26,-27,-25,-20,-21,-22,-23,-24,-26,26,26,26,119,119,]),'LEFT_CURLY_BRACKET':([9,],[28,]),'PROPERTY_IDENTIFIER_has':([9,10,26,44,45,47,51,52,53,54,55,56,57,58,59,63,71,82,83,84,96,101,109,111,123,130,132,147,],[30,30,30,30,30,30,30,-27,-25,-20,-21,-22,-23,-24,-26,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'PROPERTY_IDENTIFIER_is_Of':([9,10,26,44,45,47,51,52,53,54,55,56,57,58,59,63,71,82,83,84,96,101,109,111,123,130,132,147,],[31,31,31,31,31,31,31,-27,-25,-20,-21,-22,-23,-24,-26,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'PROPERTY_IDENTIFIER':([9,10,26,44,45,47,51,52,53,54,55,56,57,58,59,63,71,82,83,84,96,101,109,111,123,130,132,147,],[32,32,32,32,32,32,32,-27,-25,-20,-21,-22,-23,-24,-26,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'AND':([21,25,27,30,31,32,35,49,50,69,70,75,79,80,81,91,95,102,103,104,105,106,107,],[44,46,59,-28,-29,-30,59,44,-65,44,44,59,-56,44,-58,59,59,-59,44,-61,44,-63,44,]),'OR':([21,25,27,30,31,32,35,49,50,69,70,75,77,79,80,81,91,95,102,103,104,105,106,107,129,],[45,48,58,-28,-29,-30,58,45,-65,45,45,58,48,-56,45,-58,58,58,-59,45,-61,45,-63,45,135,]),'COMMA':([25,36,43,61,67,72,76,87,89,110,118,121,126,134,146,],[47,63,68,86,92,96,101,109,111,123,-71,130,132,-72,147,]),'SOME':([27,30,31,32,35,51,52,53,54,55,56,57,58,59,75,91,95,115,],[54,-28,-29,-30,54,84,-27,-25,-20,-21,-22,-23,-24,-26,99,99,54,124,]),'EXACTLY':([27,30,31,32,35,75,91,95,],[55,-28,-29,-30,55,55,55,55,]),'MIN':([27,30,31,32,35,75,91,95,],[56,-28,-29,-30,56,56,56,56,]),'MAX':([27,30,31,32,35,75,91,95,],[57,-28,-29,-30,57,57,57,57,]),'ONLY':([27,30,31,32,35,51,52,53,54,55,56,57,58,59,75,91,95,115,],[53,-28,-29,-30,53,83,-27,-25,-20,-21,-22,-23,-24,-26,100,100,53,125,]),'VALUE':([27,30,31,32,35,51,52,53,54,55,56,57,58,59,75,91,95,],[52,-28,-29,-30,52,82,-27,-25,-20,-21,-22,-23,-24,-26,52,52,52,]),'IndividualNames':([28,41,86,92,],[61,67,61,67,]),'RIGHT_PAREN':([49,50,69,70,79,80,81,102,103,104,105,106,107,116,128,129,141,145,],[79,-65,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,126,134,-73,-74,146,]),'NAMESPACEID':([52,53,54,55,56,57,58,59,62,98,99,100,],[-27,-25,-20,-21,-22,-23,-24,-26,88,117,-20,-25,]),'RIGHT_CURLY_BRACKET':([60,61,108,],[85,-76,-77,]),'DATA_TYPE':([88,117,],[110,127,]),'LEFT_BRACKET':([127,],[133,]),'LESS_THAN':([133,],[138,]),'GREATER_THAN':([133,],[139,]),'EQUALS':([133,138,139,],[140,143,144,]),'NUMBER':([137,138,139,140,143,144,],[142,-49,-50,-51,-53,-52,]),'RIGHT_BRACKET':([142,],[145,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,5,6,],[1,11,12,]),'empty':([0,5,6,7,8,13,16,17,37,38,73,94,],[3,3,3,15,18,18,18,40,40,40,40,40,]),'statement_defined_class':([4,],[5,]),'statement_primitive_class':([4,],[6,]),'EquivalentTo_possible':([4,8,],[7,16,]),'subclassof_possible':([4,7,],[8,14,]),'maybe_suclassof':([7,],[13,]),'statement_class_disjoin':([8,13,16,],[17,37,38,]),'JustDefined':([9,],[20,]),'nested':([9,26,44,45,51,82,83,84,],[21,49,69,70,80,103,105,107,]),'statement_closed_axiom_class':([9,10,],[22,34,]),'statement_enumerated_class':([9,],[23,]),'statement_covered_class':([9,],[24,]),'statement_property_identify':([9,10,26,44,45,47,51,63,71,82,83,84,96,101,109,111,123,130,132,147,],[27,35,27,27,27,75,27,91,95,27,27,27,115,115,35,91,35,35,95,95,]),'statement_covered_class_check':([9,48,],[29,78,]),'primitive_class_mandatory':([10,63,109,111,123,130,],[33,90,122,90,131,90,]),'statement_class_individuals':([17,37,38,73,94,],[39,64,65,97,113,]),'statement_class_disjoin_check':([19,68,],[42,93,]),'statement_reserved_word':([27,35,75,91,95,],[51,62,98,62,98,]),'statement_enumerated_class_check':([28,86,],[60,108,]),'statement_class_individuals_check':([41,92,],[66,112,]),'statement_defined_class_equivalent':([47,71,132,147,],[73,94,136,148,]),'closed_axiom_mandatory':([47,63,96,101,111,],[74,74,114,120,114,]),'statement_property_restriction':([47,63,96,101,111,],[76,76,76,76,76,]),'closed_axiom_restriction_combination':([119,135,],[128,141,]),'statement_operator_symbol':([133,],[137,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> Class CLASS_IDENTIFIER statement_defined_class statements','statements',4,'p_statements','Sintatico.py',6),
  ('statements -> Class CLASS_IDENTIFIER statement_defined_class','statements',3,'p_statements','Sintatico.py',7),
  ('statements -> Class CLASS_IDENTIFIER statement_primitive_class','statements',3,'p_statements','Sintatico.py',8),
  ('statements -> Class CLASS_IDENTIFIER statement_primitive_class statements','statements',4,'p_statements','Sintatico.py',9),
  ('statements -> empty','statements',1,'p_statements','Sintatico.py',10),
  ('statement_defined_class -> EquivalentTo_possible maybe_suclassof statement_class_disjoin statement_class_individuals','statement_defined_class',4,'p_statement_defined_class','Sintatico.py',14),
  ('statement_defined_class -> subclassof_possible EquivalentTo_possible statement_class_disjoin statement_class_individuals','statement_defined_class',4,'p_statement_defined_class','Sintatico.py',15),
  ('statement_primitive_class -> subclassof_possible statement_class_disjoin statement_class_individuals','statement_primitive_class',3,'p_statement_primitive_class','Sintatico.py',19),
  ('EquivalentTo_possible -> EquivalentTo JustDefined','EquivalentTo_possible',2,'p_EquivalentTo_possible','Sintatico.py',23),
  ('EquivalentTo_possible -> EquivalentTo nested','EquivalentTo_possible',2,'p_EquivalentTo_possible','Sintatico.py',24),
  ('EquivalentTo_possible -> EquivalentTo statement_closed_axiom_class','EquivalentTo_possible',2,'p_EquivalentTo_possible','Sintatico.py',25),
  ('EquivalentTo_possible -> EquivalentTo statement_enumerated_class','EquivalentTo_possible',2,'p_EquivalentTo_possible','Sintatico.py',26),
  ('EquivalentTo_possible -> EquivalentTo statement_covered_class','EquivalentTo_possible',2,'p_EquivalentTo_possible','Sintatico.py',27),
  ('maybe_suclassof -> subclassof_possible','maybe_suclassof',1,'p_maybe_suclassof','Sintatico.py',31),
  ('maybe_suclassof -> empty','maybe_suclassof',1,'p_maybe_suclassof','Sintatico.py',32),
  ('subclassof_possible -> SubClassOf primitive_class_mandatory','subclassof_possible',2,'p_subclassof_possible','Sintatico.py',36),
  ('subclassof_possible -> SubClassOf statement_closed_axiom_class','subclassof_possible',2,'p_subclassof_possible','Sintatico.py',37),
  ('JustDefined -> CLASS_IDENTIFIER AND LEFT_PAREN statement_defined_class_equivalent statement_class_individuals','JustDefined',5,'p_justDefined','Sintatico.py',41),
  ('JustDefined -> CLASS_IDENTIFIER COMMA statement_defined_class_equivalent statement_class_individuals','JustDefined',4,'p_justDefined','Sintatico.py',42),
  ('statement_reserved_word -> SOME','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',46),
  ('statement_reserved_word -> EXACTLY','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',47),
  ('statement_reserved_word -> MIN','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',48),
  ('statement_reserved_word -> MAX','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',49),
  ('statement_reserved_word -> OR','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',50),
  ('statement_reserved_word -> ONLY','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',51),
  ('statement_reserved_word -> AND','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',52),
  ('statement_reserved_word -> VALUE','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',53),
  ('statement_property_identify -> PROPERTY_IDENTIFIER_has','statement_property_identify',1,'p_statement_property_identify','Sintatico.py',57),
  ('statement_property_identify -> PROPERTY_IDENTIFIER_is_Of','statement_property_identify',1,'p_statement_property_identify','Sintatico.py',58),
  ('statement_property_identify -> PROPERTY_IDENTIFIER','statement_property_identify',1,'p_statement_property_identify','Sintatico.py',59),
  ('primitive_class_mandatory -> statement_property_identify statement_reserved_word CLASS_IDENTIFIER','primitive_class_mandatory',3,'p_primitive_class_mandatory','Sintatico.py',63),
  ('primitive_class_mandatory -> statement_property_identify statement_reserved_word CLASS_IDENTIFIER COMMA primitive_class_mandatory','primitive_class_mandatory',5,'p_primitive_class_mandatory','Sintatico.py',64),
  ('primitive_class_mandatory -> statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE','primitive_class_mandatory',4,'p_primitive_class_mandatory','Sintatico.py',65),
  ('primitive_class_mandatory -> statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE COMMA primitive_class_mandatory','primitive_class_mandatory',6,'p_primitive_class_mandatory','Sintatico.py',66),
  ('primitive_class_mandatory -> CLASS_IDENTIFIER','primitive_class_mandatory',1,'p_primitive_class_mandatory','Sintatico.py',67),
  ('primitive_class_mandatory -> CLASS_IDENTIFIER COMMA primitive_class_mandatory','primitive_class_mandatory',3,'p_primitive_class_mandatory','Sintatico.py',68),
  ('statement_class_disjoin -> empty','statement_class_disjoin',1,'p_statement_class_disjoin','Sintatico.py',72),
  ('statement_class_disjoin -> DisjointClasses statement_class_disjoin_check','statement_class_disjoin',2,'p_statement_class_disjoin','Sintatico.py',73),
  ('statement_class_disjoin_check -> CLASS_IDENTIFIER','statement_class_disjoin_check',1,'p_statement_class_disjoin_check','Sintatico.py',77),
  ('statement_class_disjoin_check -> CLASS_IDENTIFIER COMMA statement_class_disjoin_check','statement_class_disjoin_check',3,'p_statement_class_disjoin_check','Sintatico.py',78),
  ('statement_class_individuals -> empty','statement_class_individuals',1,'p_statement_class_individuals','Sintatico.py',82),
  ('statement_class_individuals -> Individuals statement_class_individuals_check','statement_class_individuals',2,'p_statement_class_individuals','Sintatico.py',83),
  ('statement_class_individuals_check -> IndividualNames','statement_class_individuals_check',1,'p_statement_class_individuals_check','Sintatico.py',87),
  ('statement_class_individuals_check -> IndividualNames COMMA statement_class_individuals_check','statement_class_individuals_check',3,'p_statement_class_individuals_check','Sintatico.py',88),
  ('statement_defined_class_equivalent -> statement_property_identify statement_reserved_word CLASS_IDENTIFIER RIGHT_PAREN','statement_defined_class_equivalent',4,'p_statement_defined_class_equivalent','Sintatico.py',93),
  ('statement_defined_class_equivalent -> statement_property_identify statement_reserved_word CLASS_IDENTIFIER RIGHT_PAREN COMMA statement_defined_class_equivalent','statement_defined_class_equivalent',6,'p_statement_defined_class_equivalent','Sintatico.py',94),
  ('statement_defined_class_equivalent -> statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET RIGHT_PAREN','statement_defined_class_equivalent',9,'p_statement_defined_class_equivalent','Sintatico.py',95),
  ('statement_defined_class_equivalent -> statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET RIGHT_PAREN COMMA statement_defined_class_equivalent','statement_defined_class_equivalent',11,'p_statement_defined_class_equivalent','Sintatico.py',96),
  ('statement_operator_symbol -> LESS_THAN','statement_operator_symbol',1,'p_statement_operator_symbol','Sintatico.py',100),
  ('statement_operator_symbol -> GREATER_THAN','statement_operator_symbol',1,'p_statement_operator_symbol','Sintatico.py',101),
  ('statement_operator_symbol -> EQUALS','statement_operator_symbol',1,'p_statement_operator_symbol','Sintatico.py',102),
  ('statement_operator_symbol -> GREATER_THAN EQUALS','statement_operator_symbol',2,'p_statement_operator_symbol','Sintatico.py',103),
  ('statement_operator_symbol -> LESS_THAN EQUALS','statement_operator_symbol',2,'p_statement_operator_symbol','Sintatico.py',104),
  ('nested -> nested AND nested','nested',3,'p_nested','Sintatico.py',109),
  ('nested -> nested OR nested','nested',3,'p_nested','Sintatico.py',110),
  ('nested -> LEFT_PAREN nested RIGHT_PAREN','nested',3,'p_nested','Sintatico.py',111),
  ('nested -> statement_property_identify statement_reserved_word nested','nested',3,'p_nested','Sintatico.py',112),
  ('nested -> statement_property_identify statement_reserved_word CLASS_IDENTIFIER','nested',3,'p_nested','Sintatico.py',113),
  ('nested -> statement_property_identify statement_reserved_word VALUE CLASS_IDENTIFIER','nested',4,'p_nested','Sintatico.py',114),
  ('nested -> statement_property_identify statement_reserved_word VALUE nested','nested',4,'p_nested','Sintatico.py',115),
  ('nested -> statement_property_identify statement_reserved_word ONLY CLASS_IDENTIFIER','nested',4,'p_nested','Sintatico.py',116),
  ('nested -> statement_property_identify statement_reserved_word ONLY nested','nested',4,'p_nested','Sintatico.py',117),
  ('nested -> statement_property_identify statement_reserved_word SOME CLASS_IDENTIFIER','nested',4,'p_nested','Sintatico.py',118),
  ('nested -> statement_property_identify statement_reserved_word SOME nested','nested',4,'p_nested','Sintatico.py',119),
  ('nested -> CLASS_IDENTIFIER','nested',1,'p_nested','Sintatico.py',120),
  ('statement_closed_axiom_class -> CLASS_IDENTIFIER COMMA closed_axiom_mandatory','statement_closed_axiom_class',3,'p_statement_closed_axiom_class','Sintatico.py',133),
  ('closed_axiom_mandatory -> CLASS_IDENTIFIER','closed_axiom_mandatory',1,'p_closed_axiom_mandatory','Sintatico.py',137),
  ('closed_axiom_mandatory -> statement_property_restriction','closed_axiom_mandatory',1,'p_closed_axiom_mandatory','Sintatico.py',138),
  ('closed_axiom_mandatory -> CLASS_IDENTIFIER COMMA closed_axiom_mandatory','closed_axiom_mandatory',3,'p_closed_axiom_mandatory','Sintatico.py',139),
  ('closed_axiom_mandatory -> statement_property_restriction COMMA closed_axiom_mandatory','closed_axiom_mandatory',3,'p_closed_axiom_mandatory','Sintatico.py',140),
  ('statement_property_restriction -> statement_property_identify SOME CLASS_IDENTIFIER','statement_property_restriction',3,'p_statement_property_restriction','Sintatico.py',144),
  ('statement_property_restriction -> statement_property_identify ONLY LEFT_PAREN closed_axiom_restriction_combination RIGHT_PAREN','statement_property_restriction',5,'p_statement_property_restriction','Sintatico.py',145),
  ('closed_axiom_restriction_combination -> CLASS_IDENTIFIER','closed_axiom_restriction_combination',1,'p_closed_axiom_restriction_combination','Sintatico.py',149),
  ('closed_axiom_restriction_combination -> CLASS_IDENTIFIER OR closed_axiom_restriction_combination','closed_axiom_restriction_combination',3,'p_closed_axiom_restriction_combination','Sintatico.py',150),
  ('statement_enumerated_class -> LEFT_CURLY_BRACKET statement_enumerated_class_check RIGHT_CURLY_BRACKET','statement_enumerated_class',3,'p_statement_enumerated_class','Sintatico.py',155),
  ('statement_enumerated_class_check -> IndividualNames','statement_enumerated_class_check',1,'p_statement_enumerated_class_check','Sintatico.py',159),
  ('statement_enumerated_class_check -> IndividualNames COMMA statement_enumerated_class_check','statement_enumerated_class_check',3,'p_statement_enumerated_class_check','Sintatico.py',160),
  ('statement_covered_class -> statement_covered_class_check','statement_covered_class',1,'p_statement_covered_class','Sintatico.py',165),
  ('statement_covered_class_check -> CLASS_IDENTIFIER','statement_covered_class_check',1,'p_statement_covered_class_check','Sintatico.py',169),
  ('statement_covered_class_check -> CLASS_IDENTIFIER OR statement_covered_class_check','statement_covered_class_check',3,'p_statement_covered_class_check','Sintatico.py',170),
  ('empty -> <empty>','empty',0,'p_empty','Sintatico.py',175),
]
