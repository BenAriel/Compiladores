
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALL AND CLASS_IDENTIFIER COMMA Class DATA_TYPE DIVIDE DisjointClasses DisjointWith EQUALS EXACTLY EquivalentTo GREATER_THAN IndividualNames Individuals LEFT_BRACKET LEFT_CURLY_BRACKET LEFT_PAREN LESS_THAN Literal MAX MIN MINUS NAMESPACEID NCName NMTOKEN NOT NUMBER Name ONLY OR PLUS PROPERTY_IDENTIFIER PROPERTY_IDENTIFIER_has PROPERTY_IDENTIFIER_is_Of PlainLiteral RIGHT_BRACKET RIGHT_CURLY_BRACKET RIGHT_PAREN SOME SubClassOf THAT TIMES VALUE XMLLiteral anyURI base64Binary boolean byte dateTime dateTimeStamp decimal double float hexBinary int integer langString languague long negativeInteger nonNegativeInteger owl rational rdf rdfs real string xsdstatements : Class CLASS_IDENTIFIER statement_defined_class statements\n| Class CLASS_IDENTIFIER statement_defined_class\n| Class CLASS_IDENTIFIER statement_primitive_class\n| Class CLASS_IDENTIFIER statement_primitive_class statements\n| emptystatement_defined_class : EquivalentTo_possible maybe_suclassof statement_class_disjoin statement_class_individuals\n| subclassof_possible EquivalentTo_possible statement_class_disjoin statement_class_individualsstatement_primitive_class : subclassof_possible statement_class_disjoin statement_class_individualsEquivalentTo_possible : EquivalentTo JustDefined\n| EquivalentTo nested\n| EquivalentTo statement_closed_axiom_class\n| EquivalentTo statement_enumerated_class\n| EquivalentTo statement_covered_class\nmaybe_suclassof : subclassof_possible\n| emptysubclassof_possible : SubClassOf nested\n| SubClassOf statement_closed_axiom_class\n| SubClassOf statement_enumerated_class\n| SubClassOf statement_covered_class\n| SubClassOf primitive_class_mandatoryJustDefined : CLASS_IDENTIFIER COMMA expression statement_class_disjoin statement_class_individuals\n| CLASS_IDENTIFIER AND expression statement_class_disjoin statement_class_individuals\n| expression statement_class_disjoin statement_class_individuals\n| CLASS_IDENTIFIER\n| emptystatement_reserved_word : SOME\n| EXACTLY\n| MIN\n| MAX\n| OR\n| AND\n| VALUEstatement_others_reserved_word : SOME\n| ONLY\n| MIN\n| EXACTLY\n| OR\n| MAX\n| ANDstatement_property_identify : PROPERTY_IDENTIFIER_has\n| PROPERTY_IDENTIFIER_is_Of\n| PROPERTY_IDENTIFIERprimitive_class_mandatory : CLASS_IDENTIFIER COMMA expression statement_class_disjoin statement_class_individuals\n| CLASS_IDENTIFIER AND expression statement_class_disjoin statement_class_individuals\n| expression statement_class_disjoin statement_class_individuals\n| CLASS_IDENTIFIER\n| empty  statement_class_disjoin : empty\n| DisjointClasses statement_class_disjoin_check\n| DisjointWith statement_class_disjoin_checkstatement_class_disjoin_check : CLASS_IDENTIFIER\n| CLASS_IDENTIFIER COMMA statement_class_disjoin_checkstatement_class_individuals : empty\n| Individuals statement_class_individuals_checkstatement_class_individuals_check : IndividualNames\n| IndividualNames COMMA statement_class_individuals_checkstatement_defined_class_equivalent : statement_property_identify statement_reserved_word CLASS_IDENTIFIER RIGHT_PAREN\n| statement_property_identify statement_reserved_word CLASS_IDENTIFIER RIGHT_PAREN COMMA statement_defined_class_equivalent\n                                      | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET RIGHT_PAREN\n                                      | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET RIGHT_PAREN COMMA statement_defined_class_equivalent statement_operator_symbol : LESS_THAN\n| GREATER_THAN\n| EQUALS\n|  GREATER_THAN EQUALS\n| LESS_THAN EQUALSusually_inside_paren : statement_property_identify statement_reserved_word CLASS_IDENTIFIER\n| statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE\n| statement_property_identify statement_reserved_word NUMBER NAMESPACEID DATA_TYPE\n| statement_property_identify statement_reserved_word NUMBER CLASS_IDENTIFIER\n| statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKETusually_others_paren : statement_property_identify statement_others_reserved_word CLASS_IDENTIFIER\n| statement_property_identify statement_others_reserved_word LEFT_PAREN usually_others_others_paren\n| statement_property_identify statement_others_reserved_word NAMESPACEID DATA_TYPE\n| statement_property_identify statement_others_reserved_word NUMBER NAMESPACEID DATA_TYPE\n| statement_property_identify statement_others_reserved_word NUMBER CLASS_IDENTIFIER\n| statement_property_identify statement_others_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKETusually_others_others_paren : CLASS_IDENTIFIER RIGHT_PAREN\n| CLASS_IDENTIFIER OR usually_others_others_parensimple_paren : LEFT_PAREN usually_inside_paren RIGHT_PARENsimple_other_paren : LEFT_PAREN usually_others_paren RIGHT_PARENexpression : usually_inside_paren\n| usually_inside_paren COMMA expression\n| simple_paren\n| simple_paren COMMA expression\n| simple_paren AND expressionother_expression : usually_inside_paren\n| usually_others_paren\n| usually_inside_paren COMMA other_expression\n| usually_others_paren COMMA other_expression\n| simple_other_paren\n| simple_other_paren COMMA other_expression\n| simple_other_paren AND other_expression\n| usually_others_paren AND other_expression\nnested : CLASS_IDENTIFIER AND nested_descriptions\n|  CLASS_IDENTIFIER COMMA nested_descriptionsnested_descriptions : nested_descriptions AND nested_descriptions\n| nested_descriptions OR nested_descriptions\n| LEFT_PAREN nested_descriptions RIGHT_PAREN\n| statement_property_identify statement_others_reserved_word nested_descriptions\n| statement_property_identify statement_others_reserved_word CLASS_IDENTIFIER\n| statement_property_identify statement_others_reserved_word VALUE CLASS_IDENTIFIER\n| statement_property_identify statement_others_reserved_word VALUE IndividualNames\n| statement_property_identify VALUE IndividualNames\n| statement_property_identify VALUE CLASS_IDENTIFIER\n| statement_property_identify statement_others_reserved_word VALUE nested_descriptions\n| statement_property_identify statement_others_reserved_word NUMBER nested_descriptions\n| statement_property_identify statement_others_reserved_word ONLY CLASS_IDENTIFIER\n| statement_property_identify statement_others_reserved_word ONLY nested_descriptions\n| statement_property_identify statement_others_reserved_word SOME CLASS_IDENTIFIER\n| statement_property_identify statement_others_reserved_word SOME nested_descriptions\n| CLASS_IDENTIFIERstatement_closed_axiom_class : CLASS_IDENTIFIER COMMA other_expression \n|  CLASS_IDENTIFIER AND other_expression\n|  CLASS_IDENTIFIER other_expressionclosed_axiom_restriction_combination : CLASS_IDENTIFIER\n| CLASS_IDENTIFIER OR closed_axiom_restriction_combinationstatement_enumerated_class : LEFT_CURLY_BRACKET statement_enumerated_class_check RIGHT_CURLY_BRACKETstatement_enumerated_class_check : IndividualNames\n| IndividualNames COMMA statement_enumerated_class_checkstatement_covered_class : statement_covered_class_checkstatement_covered_class_check : CLASS_IDENTIFIER\n| CLASS_IDENTIFIER OR statement_covered_class_checkempty :'
    
_lr_action_items = {'Class':([0,5,6,7,8,9,10,13,14,15,16,17,18,21,22,23,24,25,26,27,28,30,31,32,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,56,58,59,60,63,80,81,82,83,84,86,87,88,89,90,93,94,95,96,97,113,114,116,117,118,119,122,123,125,126,127,129,130,144,145,146,147,148,149,150,154,162,164,165,168,169,170,171,173,175,176,177,183,184,185,186,188,190,192,193,195,198,199,200,201,202,203,204,205,206,208,211,217,219,225,226,],[2,2,2,-123,-123,-123,-123,-123,-14,-15,-123,-123,-48,-9,-10,-11,-12,-13,-24,-123,-25,-120,-81,-83,-16,-17,-18,-19,-20,-46,-123,-47,-123,-123,-8,-53,-49,-51,-50,-114,-86,-87,-90,-123,-123,-6,-7,-54,-55,-111,-123,-95,-112,-81,-123,-94,-113,-121,-122,-23,-117,-82,-84,-85,-66,-79,-123,-81,-123,-45,-52,-123,-123,-88,-89,-93,-91,-92,-71,-80,-67,-69,-123,-123,-56,-21,-96,-97,-98,-99,-71,-103,-104,-22,-72,-73,-75,-68,-44,-43,-101,-102,-105,-106,-75,-107,-108,-109,-110,-77,-74,-100,-78,-70,-76,]),'$end':([0,1,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,30,31,32,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,56,58,59,60,63,80,81,82,83,84,86,87,88,89,90,93,94,95,96,97,113,114,116,117,118,119,122,123,125,126,127,129,130,144,145,146,147,148,149,150,154,162,164,165,168,169,170,171,173,175,176,177,183,184,185,186,188,190,192,193,195,198,199,200,201,202,203,204,205,206,208,211,217,219,225,226,],[-123,0,-5,-2,-3,-123,-123,-123,-123,-1,-4,-123,-14,-15,-123,-123,-48,-9,-10,-11,-12,-13,-24,-123,-25,-120,-81,-83,-16,-17,-18,-19,-20,-46,-123,-47,-123,-123,-8,-53,-49,-51,-50,-114,-86,-87,-90,-123,-123,-6,-7,-54,-55,-111,-123,-95,-112,-81,-123,-94,-113,-121,-122,-23,-117,-82,-84,-85,-66,-79,-123,-81,-123,-45,-52,-123,-123,-88,-89,-93,-91,-92,-71,-80,-67,-69,-123,-123,-56,-21,-96,-97,-98,-99,-71,-103,-104,-22,-72,-73,-75,-68,-44,-43,-101,-102,-105,-106,-75,-107,-108,-109,-110,-77,-74,-100,-78,-70,-76,]),'CLASS_IDENTIFIER':([2,9,10,19,20,54,55,57,69,70,71,72,73,74,75,76,78,79,85,91,103,104,105,106,107,108,109,110,121,124,131,132,134,136,137,138,139,140,141,142,143,151,153,155,156,157,158,159,160,178,179,180,181,182,196,197,209,218,],[4,26,43,52,52,86,86,96,119,-26,-27,-28,-29,-30,-31,-32,86,86,52,86,150,-26,-27,-28,-29,-30,-31,-34,164,86,86,86,86,177,184,-26,-28,-27,-30,-29,-31,187,190,-33,-35,-36,-37,-38,-39,198,202,203,205,207,217,184,187,86,]),'EquivalentTo':([4,8,10,18,30,31,32,38,39,40,41,42,43,44,45,49,51,52,53,56,58,59,60,80,83,84,86,88,89,94,95,96,97,114,116,117,118,119,122,123,125,126,127,129,145,146,147,148,149,150,154,162,164,165,168,169,171,173,175,176,177,183,184,186,188,190,192,193,195,198,199,200,201,202,203,204,205,206,208,211,217,219,225,226,],[9,9,-123,-48,-120,-81,-83,-16,-17,-18,-19,-20,-46,-123,-47,-53,-49,-51,-50,-114,-86,-87,-90,-123,-54,-55,-111,-95,-112,-94,-113,-121,-122,-117,-82,-84,-85,-66,-79,-123,-81,-123,-45,-52,-88,-89,-93,-91,-92,-71,-80,-67,-69,-123,-123,-56,-96,-97,-98,-99,-71,-103,-104,-72,-73,-75,-68,-44,-43,-101,-102,-105,-106,-75,-107,-108,-109,-110,-77,-74,-100,-78,-70,-76,]),'SubClassOf':([4,7,9,18,21,22,23,24,25,26,27,28,30,31,32,49,51,52,53,56,58,59,60,63,83,84,86,87,88,89,90,93,94,95,96,97,113,114,116,117,118,119,122,129,130,144,145,146,147,148,149,150,154,162,164,169,170,171,173,175,176,177,183,184,185,186,188,190,192,198,199,200,201,202,203,204,205,206,208,211,217,219,225,226,],[10,10,-123,-48,-9,-10,-11,-12,-13,-24,-123,-25,-120,-81,-83,-53,-49,-51,-50,-114,-86,-87,-90,-123,-54,-55,-111,-123,-95,-112,-81,-123,-94,-113,-121,-122,-23,-117,-82,-84,-85,-66,-79,-52,-123,-123,-88,-89,-93,-91,-92,-71,-80,-67,-69,-56,-21,-96,-97,-98,-99,-71,-103,-104,-22,-72,-73,-75,-68,-101,-102,-105,-106,-75,-107,-108,-109,-110,-77,-74,-100,-78,-70,-76,]),'DisjointClasses':([7,8,9,10,13,14,15,16,18,21,22,23,24,25,26,27,28,30,31,32,38,39,40,41,42,43,44,45,49,51,52,53,56,58,59,60,63,80,83,84,86,87,88,89,90,93,94,95,96,97,113,114,116,117,118,119,122,123,125,126,127,129,130,144,145,146,147,148,149,150,154,162,164,165,168,169,170,171,173,175,176,177,183,184,185,186,188,190,192,193,195,198,199,200,201,202,203,204,205,206,208,211,217,219,225,226,],[-123,19,-123,-123,19,-14,-15,19,-48,-9,-10,-11,-12,-13,-24,19,-25,-120,-81,-83,-16,-17,-18,-19,-20,-46,19,-47,-53,-49,-51,-50,-114,-86,-87,-90,-123,-123,-54,-55,-111,19,-95,-112,-81,19,-94,-113,-121,-122,-23,-117,-82,-84,-85,-66,-79,19,-81,19,-45,-52,-123,-123,-88,-89,-93,-91,-92,-71,-80,-67,-69,-123,-123,-56,-21,-96,-97,-98,-99,-71,-103,-104,-22,-72,-73,-75,-68,-44,-43,-101,-102,-105,-106,-75,-107,-108,-109,-110,-77,-74,-100,-78,-70,-76,]),'DisjointWith':([7,8,9,10,13,14,15,16,18,21,22,23,24,25,26,27,28,30,31,32,38,39,40,41,42,43,44,45,49,51,52,53,56,58,59,60,63,80,83,84,86,87,88,89,90,93,94,95,96,97,113,114,116,117,118,119,122,123,125,126,127,129,130,144,145,146,147,148,149,150,154,162,164,165,168,169,170,171,173,175,176,177,183,184,185,186,188,190,192,193,195,198,199,200,201,202,203,204,205,206,208,211,217,219,225,226,],[-123,20,-123,-123,20,-14,-15,20,-48,-9,-10,-11,-12,-13,-24,20,-25,-120,-81,-83,-16,-17,-18,-19,-20,-46,20,-47,-53,-49,-51,-50,-114,-86,-87,-90,-123,-123,-54,-55,-111,20,-95,-112,-81,20,-94,-113,-121,-122,-23,-117,-82,-84,-85,-66,-79,20,-81,20,-45,-52,-123,-123,-88,-89,-93,-91,-92,-71,-80,-67,-69,-123,-123,-56,-21,-96,-97,-98,-99,-71,-103,-104,-22,-72,-73,-75,-68,-44,-43,-101,-102,-105,-106,-75,-107,-108,-109,-110,-77,-74,-100,-78,-70,-76,]),'Individuals':([7,8,9,10,13,14,15,16,17,18,21,22,23,24,25,26,27,28,30,31,32,38,39,40,41,42,43,44,45,46,47,49,51,52,53,56,58,59,60,63,80,83,84,86,87,88,89,90,93,94,95,96,97,113,114,116,117,118,119,122,123,125,126,127,129,130,144,145,146,147,148,149,150,154,162,164,165,168,169,170,171,173,175,176,177,183,184,185,186,188,190,192,193,195,198,199,200,201,202,203,204,205,206,208,211,217,219,225,226,],[-123,-123,-123,-123,-123,-14,-15,-123,50,-48,-9,-10,-11,-12,-13,-24,-123,-25,-120,-81,-83,-16,-17,-18,-19,-20,-46,-123,-47,50,50,-53,-49,-51,-50,-114,-86,-87,-90,50,50,-54,-55,-111,-123,-95,-112,-81,-123,-94,-113,-121,-122,-23,-117,-82,-84,-85,-66,-79,-123,-81,-123,-45,-52,50,50,-88,-89,-93,-91,-92,-71,-80,-67,-69,50,50,-56,-21,-96,-97,-98,-99,-71,-103,-104,-22,-72,-73,-75,-68,-44,-43,-101,-102,-105,-106,-75,-107,-108,-109,-110,-77,-74,-100,-78,-70,-76,]),'LEFT_CURLY_BRACKET':([9,10,],[29,29,]),'LEFT_PAREN':([9,10,26,43,54,55,66,67,68,78,79,91,98,99,100,101,102,103,104,105,106,107,108,109,110,124,131,132,133,134,136,138,139,140,141,142,143,155,156,157,158,159,160,167,178,179,180,181,182,196,218,],[34,34,62,62,91,91,34,34,34,124,124,134,62,62,62,62,62,151,-33,-36,-35,-38,-37,-39,-34,134,134,134,174,134,182,-33,-35,-36,-37,-38,-39,-33,-35,-36,-37,-38,-39,194,134,134,134,134,134,134,134,]),'PROPERTY_IDENTIFIER_has':([9,10,26,34,43,54,55,62,66,67,68,78,79,91,98,99,100,101,102,110,124,131,132,133,134,136,138,139,140,141,142,143,155,156,157,158,159,160,167,174,178,179,180,181,182,194,196,218,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-34,35,35,35,35,35,35,-33,-35,-36,-37,-38,-39,-33,-35,-36,-37,-38,-39,35,35,35,35,35,35,35,35,35,35,]),'PROPERTY_IDENTIFIER_is_Of':([9,10,26,34,43,54,55,62,66,67,68,78,79,91,98,99,100,101,102,110,124,131,132,133,134,136,138,139,140,141,142,143,155,156,157,158,159,160,167,174,178,179,180,181,182,194,196,218,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-34,36,36,36,36,36,36,-33,-35,-36,-37,-38,-39,-33,-35,-36,-37,-38,-39,36,36,36,36,36,36,36,36,36,36,]),'PROPERTY_IDENTIFIER':([9,10,26,34,43,54,55,62,66,67,68,78,79,91,98,99,100,101,102,110,124,131,132,133,134,136,138,139,140,141,142,143,155,156,157,158,159,160,167,174,178,179,180,181,182,194,196,218,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-34,37,37,37,37,37,37,-33,-35,-36,-37,-38,-39,-33,-35,-36,-37,-38,-39,37,37,37,37,37,37,37,37,37,37,]),'COMMA':([26,31,32,43,52,58,59,60,65,84,90,119,122,125,150,154,162,164,177,186,188,190,192,202,208,211,219,225,226,],[54,66,67,79,85,98,99,101,115,128,133,-66,-79,167,-71,-80,-67,-69,-71,-72,-73,-75,-68,-75,-77,-74,-78,-70,-76,]),'AND':([26,32,33,35,36,37,43,59,60,61,86,88,92,94,112,122,135,150,154,166,171,172,173,175,176,177,183,184,186,188,190,198,199,200,201,202,203,204,205,206,207,208,211,216,217,219,226,],[55,68,75,-40,-41,-42,78,100,102,109,-111,131,143,131,160,-79,131,-71,-80,143,131,160,131,-98,131,-71,-103,-104,-72,-73,-75,-101,-102,131,131,-75,-107,131,-109,131,-111,-77,-74,143,-100,-78,-76,]),'OR':([26,33,35,36,37,43,61,86,88,92,94,96,112,135,166,171,172,173,175,176,177,183,184,187,198,199,200,201,202,203,204,205,206,207,216,217,],[57,74,-40,-41,-42,57,108,-111,132,141,132,57,158,132,141,132,158,132,-98,132,-100,-103,-104,209,-101,-102,132,132,-111,-107,132,-109,132,209,141,-100,]),'IndividualNames':([29,50,115,128,137,178,197,],[65,84,65,84,183,199,183,]),'SOME':([33,35,36,37,61,92,110,112,136,138,139,140,141,142,143,155,156,157,158,159,160,166,172,196,216,],[70,-40,-41,-42,104,138,-34,155,181,-33,-35,-36,-37,-38,-39,-33,-35,-36,-37,-38,-39,138,155,181,138,]),'EXACTLY':([33,35,36,37,61,92,112,166,172,216,],[71,-40,-41,-42,105,140,157,140,157,140,]),'MIN':([33,35,36,37,61,92,112,166,172,216,],[72,-40,-41,-42,106,139,156,139,156,139,]),'MAX':([33,35,36,37,61,92,112,166,172,216,],[73,-40,-41,-42,107,142,159,142,159,142,]),'VALUE':([33,35,36,37,61,92,110,136,138,139,140,141,142,143,155,156,157,158,159,160,166,172,196,216,],[76,-40,-41,-42,76,137,-34,178,-33,-35,-36,-37,-38,-39,-33,-35,-36,-37,-38,-39,137,197,178,76,]),'ONLY':([35,36,37,61,92,110,112,136,138,139,140,141,142,143,155,156,157,158,159,160,166,172,196,216,],[-40,-41,-42,110,110,-34,110,180,-33,-35,-36,-37,-38,-39,-33,-35,-36,-37,-38,-39,110,110,180,110,]),'RIGHT_CURLY_BRACKET':([64,65,161,],[114,-118,-119,]),'NAMESPACEID':([69,70,71,72,73,74,75,76,103,104,105,106,107,108,109,110,121,136,137,138,139,140,141,142,143,153,155,156,157,158,159,160,179,],[120,-26,-27,-28,-29,-30,-31,-32,152,-26,-27,-28,-29,-30,-31,-34,163,152,-32,-26,-28,-27,-30,-29,-31,189,-33,-35,-36,-37,-38,-39,189,]),'NUMBER':([69,70,71,72,73,74,75,76,103,104,105,106,107,108,109,110,136,137,138,139,140,141,142,143,155,156,157,158,159,160,196,212,213,214,215,220,222,223,],[121,-26,-27,-28,-29,-30,-31,-32,153,-26,-27,-28,-29,-30,-31,-34,179,-32,-26,-28,-27,-30,-29,-31,-33,-35,-36,-37,-38,-39,218,221,-61,-62,-63,224,-65,-64,]),'RIGHT_PAREN':([77,86,111,119,135,150,162,164,171,173,175,176,177,183,184,186,187,188,190,192,198,199,200,201,202,203,204,205,206,207,208,211,217,219,225,226,],[122,-111,154,-66,175,-71,-67,-69,-96,-97,-98,-99,-71,-103,-104,-72,208,-73,-75,-68,-101,-102,-105,-106,-75,-107,-108,-109,-110,208,-77,-74,-100,-78,-70,-76,]),'DATA_TYPE':([120,152,163,189,],[162,188,192,211,]),'LEFT_BRACKET':([162,188,],[191,210,]),'LESS_THAN':([191,210,],[213,213,]),'GREATER_THAN':([191,210,],[214,214,]),'EQUALS':([191,210,213,214,],[215,215,222,223,]),'RIGHT_BRACKET':([221,224,],[225,226,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,5,6,],[1,11,12,]),'empty':([0,5,6,7,8,9,10,13,16,17,27,44,46,47,63,80,87,93,123,126,130,144,165,168,],[3,3,3,15,18,28,45,18,18,49,18,18,49,49,49,49,18,18,18,18,49,49,49,49,]),'statement_defined_class':([4,],[5,]),'statement_primitive_class':([4,],[6,]),'EquivalentTo_possible':([4,8,],[7,16,]),'subclassof_possible':([4,7,],[8,14,]),'maybe_suclassof':([7,],[13,]),'statement_class_disjoin':([8,13,16,27,44,87,93,123,126,],[17,46,47,63,80,130,144,165,168,]),'JustDefined':([9,],[21,]),'nested':([9,10,],[22,38,]),'statement_closed_axiom_class':([9,10,],[23,39,]),'statement_enumerated_class':([9,10,],[24,40,]),'statement_covered_class':([9,10,],[25,41,]),'expression':([9,10,54,55,66,67,68,78,79,133,167,],[27,44,87,93,116,117,118,123,126,116,116,]),'statement_covered_class_check':([9,10,57,],[30,30,97,]),'usually_inside_paren':([9,10,26,34,43,54,55,66,67,68,78,79,91,98,99,100,101,102,124,133,167,174,194,],[31,31,58,77,58,90,90,31,31,31,125,125,77,58,58,58,58,58,77,90,125,77,77,]),'simple_paren':([9,10,54,55,66,67,68,78,79,133,167,],[32,32,32,32,32,32,32,32,32,32,32,]),'statement_property_identify':([9,10,26,34,43,54,55,62,66,67,68,78,79,91,98,99,100,101,102,124,131,132,133,134,136,167,174,178,179,180,181,182,194,196,218,],[33,33,61,33,61,92,92,112,33,33,33,92,92,92,61,61,61,61,61,166,172,172,61,172,172,61,61,172,172,172,172,172,216,172,172,]),'primitive_class_mandatory':([10,],[42,]),'statement_class_individuals':([17,46,47,63,80,130,144,165,168,],[48,81,82,113,127,170,185,193,195,]),'statement_class_disjoin_check':([19,20,85,],[51,53,129,]),'other_expression':([26,43,54,55,78,79,98,99,100,101,102,133,167,],[56,56,89,95,95,89,145,146,147,148,149,145,145,]),'usually_others_paren':([26,43,54,55,62,78,79,91,98,99,100,101,102,124,133,167,174,194,],[59,59,59,59,111,59,59,111,59,59,59,59,59,111,59,59,111,111,]),'simple_other_paren':([26,43,54,55,78,79,98,99,100,101,102,133,167,],[60,60,60,60,60,60,60,60,60,60,60,60,60,]),'statement_enumerated_class_check':([29,115,],[64,161,]),'statement_reserved_word':([33,61,92,166,216,],[69,69,69,69,69,]),'statement_class_individuals_check':([50,128,],[83,169,]),'nested_descriptions':([54,55,78,79,91,124,131,132,134,136,178,179,180,181,182,196,218,],[88,94,94,88,135,135,171,173,135,176,200,201,204,206,135,176,201,]),'statement_others_reserved_word':([61,92,112,166,172,216,],[103,136,103,136,196,103,]),'usually_others_others_paren':([151,182,209,],[186,186,219,]),'statement_operator_symbol':([191,210,],[212,220,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> Class CLASS_IDENTIFIER statement_defined_class statements','statements',4,'p_statements','Sintatico.py',7),
  ('statements -> Class CLASS_IDENTIFIER statement_defined_class','statements',3,'p_statements','Sintatico.py',8),
  ('statements -> Class CLASS_IDENTIFIER statement_primitive_class','statements',3,'p_statements','Sintatico.py',9),
  ('statements -> Class CLASS_IDENTIFIER statement_primitive_class statements','statements',4,'p_statements','Sintatico.py',10),
  ('statements -> empty','statements',1,'p_statements','Sintatico.py',11),
  ('statement_defined_class -> EquivalentTo_possible maybe_suclassof statement_class_disjoin statement_class_individuals','statement_defined_class',4,'p_statement_defined_class','Sintatico.py',15),
  ('statement_defined_class -> subclassof_possible EquivalentTo_possible statement_class_disjoin statement_class_individuals','statement_defined_class',4,'p_statement_defined_class','Sintatico.py',16),
  ('statement_primitive_class -> subclassof_possible statement_class_disjoin statement_class_individuals','statement_primitive_class',3,'p_statement_primitive_class','Sintatico.py',19),
  ('EquivalentTo_possible -> EquivalentTo JustDefined','EquivalentTo_possible',2,'p_EquivalentTo_possible','Sintatico.py',22),
  ('EquivalentTo_possible -> EquivalentTo nested','EquivalentTo_possible',2,'p_EquivalentTo_possible','Sintatico.py',23),
  ('EquivalentTo_possible -> EquivalentTo statement_closed_axiom_class','EquivalentTo_possible',2,'p_EquivalentTo_possible','Sintatico.py',24),
  ('EquivalentTo_possible -> EquivalentTo statement_enumerated_class','EquivalentTo_possible',2,'p_EquivalentTo_possible','Sintatico.py',25),
  ('EquivalentTo_possible -> EquivalentTo statement_covered_class','EquivalentTo_possible',2,'p_EquivalentTo_possible','Sintatico.py',26),
  ('maybe_suclassof -> subclassof_possible','maybe_suclassof',1,'p_maybe_suclassof','Sintatico.py',31),
  ('maybe_suclassof -> empty','maybe_suclassof',1,'p_maybe_suclassof','Sintatico.py',32),
  ('subclassof_possible -> SubClassOf nested','subclassof_possible',2,'p_subclassof_possible','Sintatico.py',36),
  ('subclassof_possible -> SubClassOf statement_closed_axiom_class','subclassof_possible',2,'p_subclassof_possible','Sintatico.py',37),
  ('subclassof_possible -> SubClassOf statement_enumerated_class','subclassof_possible',2,'p_subclassof_possible','Sintatico.py',38),
  ('subclassof_possible -> SubClassOf statement_covered_class','subclassof_possible',2,'p_subclassof_possible','Sintatico.py',39),
  ('subclassof_possible -> SubClassOf primitive_class_mandatory','subclassof_possible',2,'p_subclassof_possible','Sintatico.py',40),
  ('JustDefined -> CLASS_IDENTIFIER COMMA expression statement_class_disjoin statement_class_individuals','JustDefined',5,'p_justDefined','Sintatico.py',44),
  ('JustDefined -> CLASS_IDENTIFIER AND expression statement_class_disjoin statement_class_individuals','JustDefined',5,'p_justDefined','Sintatico.py',45),
  ('JustDefined -> expression statement_class_disjoin statement_class_individuals','JustDefined',3,'p_justDefined','Sintatico.py',46),
  ('JustDefined -> CLASS_IDENTIFIER','JustDefined',1,'p_justDefined','Sintatico.py',47),
  ('JustDefined -> empty','JustDefined',1,'p_justDefined','Sintatico.py',48),
  ('statement_reserved_word -> SOME','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',53),
  ('statement_reserved_word -> EXACTLY','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',54),
  ('statement_reserved_word -> MIN','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',55),
  ('statement_reserved_word -> MAX','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',56),
  ('statement_reserved_word -> OR','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',57),
  ('statement_reserved_word -> AND','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',58),
  ('statement_reserved_word -> VALUE','statement_reserved_word',1,'p_statement_reserved_word','Sintatico.py',59),
  ('statement_others_reserved_word -> SOME','statement_others_reserved_word',1,'p_statement_others_reserved_word','Sintatico.py',63),
  ('statement_others_reserved_word -> ONLY','statement_others_reserved_word',1,'p_statement_others_reserved_word','Sintatico.py',64),
  ('statement_others_reserved_word -> MIN','statement_others_reserved_word',1,'p_statement_others_reserved_word','Sintatico.py',65),
  ('statement_others_reserved_word -> EXACTLY','statement_others_reserved_word',1,'p_statement_others_reserved_word','Sintatico.py',66),
  ('statement_others_reserved_word -> OR','statement_others_reserved_word',1,'p_statement_others_reserved_word','Sintatico.py',67),
  ('statement_others_reserved_word -> MAX','statement_others_reserved_word',1,'p_statement_others_reserved_word','Sintatico.py',68),
  ('statement_others_reserved_word -> AND','statement_others_reserved_word',1,'p_statement_others_reserved_word','Sintatico.py',69),
  ('statement_property_identify -> PROPERTY_IDENTIFIER_has','statement_property_identify',1,'p_statement_property_identify','Sintatico.py',73),
  ('statement_property_identify -> PROPERTY_IDENTIFIER_is_Of','statement_property_identify',1,'p_statement_property_identify','Sintatico.py',74),
  ('statement_property_identify -> PROPERTY_IDENTIFIER','statement_property_identify',1,'p_statement_property_identify','Sintatico.py',75),
  ('primitive_class_mandatory -> CLASS_IDENTIFIER COMMA expression statement_class_disjoin statement_class_individuals','primitive_class_mandatory',5,'p_primitive_class_mandatory','Sintatico.py',79),
  ('primitive_class_mandatory -> CLASS_IDENTIFIER AND expression statement_class_disjoin statement_class_individuals','primitive_class_mandatory',5,'p_primitive_class_mandatory','Sintatico.py',80),
  ('primitive_class_mandatory -> expression statement_class_disjoin statement_class_individuals','primitive_class_mandatory',3,'p_primitive_class_mandatory','Sintatico.py',81),
  ('primitive_class_mandatory -> CLASS_IDENTIFIER','primitive_class_mandatory',1,'p_primitive_class_mandatory','Sintatico.py',82),
  ('primitive_class_mandatory -> empty','primitive_class_mandatory',1,'p_primitive_class_mandatory','Sintatico.py',83),
  ('statement_class_disjoin -> empty','statement_class_disjoin',1,'p_statement_class_disjoin','Sintatico.py',88),
  ('statement_class_disjoin -> DisjointClasses statement_class_disjoin_check','statement_class_disjoin',2,'p_statement_class_disjoin','Sintatico.py',89),
  ('statement_class_disjoin -> DisjointWith statement_class_disjoin_check','statement_class_disjoin',2,'p_statement_class_disjoin','Sintatico.py',90),
  ('statement_class_disjoin_check -> CLASS_IDENTIFIER','statement_class_disjoin_check',1,'p_statement_class_disjoin_check','Sintatico.py',94),
  ('statement_class_disjoin_check -> CLASS_IDENTIFIER COMMA statement_class_disjoin_check','statement_class_disjoin_check',3,'p_statement_class_disjoin_check','Sintatico.py',95),
  ('statement_class_individuals -> empty','statement_class_individuals',1,'p_statement_class_individuals','Sintatico.py',99),
  ('statement_class_individuals -> Individuals statement_class_individuals_check','statement_class_individuals',2,'p_statement_class_individuals','Sintatico.py',100),
  ('statement_class_individuals_check -> IndividualNames','statement_class_individuals_check',1,'p_statement_class_individuals_check','Sintatico.py',104),
  ('statement_class_individuals_check -> IndividualNames COMMA statement_class_individuals_check','statement_class_individuals_check',3,'p_statement_class_individuals_check','Sintatico.py',105),
  ('statement_defined_class_equivalent -> statement_property_identify statement_reserved_word CLASS_IDENTIFIER RIGHT_PAREN','statement_defined_class_equivalent',4,'p_statement_defined_class_equivalent','Sintatico.py',109),
  ('statement_defined_class_equivalent -> statement_property_identify statement_reserved_word CLASS_IDENTIFIER RIGHT_PAREN COMMA statement_defined_class_equivalent','statement_defined_class_equivalent',6,'p_statement_defined_class_equivalent','Sintatico.py',110),
  ('statement_defined_class_equivalent -> statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET RIGHT_PAREN','statement_defined_class_equivalent',9,'p_statement_defined_class_equivalent','Sintatico.py',111),
  ('statement_defined_class_equivalent -> statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET RIGHT_PAREN COMMA statement_defined_class_equivalent','statement_defined_class_equivalent',11,'p_statement_defined_class_equivalent','Sintatico.py',112),
  ('statement_operator_symbol -> LESS_THAN','statement_operator_symbol',1,'p_statement_operator_symbol','Sintatico.py',116),
  ('statement_operator_symbol -> GREATER_THAN','statement_operator_symbol',1,'p_statement_operator_symbol','Sintatico.py',117),
  ('statement_operator_symbol -> EQUALS','statement_operator_symbol',1,'p_statement_operator_symbol','Sintatico.py',118),
  ('statement_operator_symbol -> GREATER_THAN EQUALS','statement_operator_symbol',2,'p_statement_operator_symbol','Sintatico.py',119),
  ('statement_operator_symbol -> LESS_THAN EQUALS','statement_operator_symbol',2,'p_statement_operator_symbol','Sintatico.py',120),
  ('usually_inside_paren -> statement_property_identify statement_reserved_word CLASS_IDENTIFIER','usually_inside_paren',3,'p_usually_inside_paren','Sintatico.py',125),
  ('usually_inside_paren -> statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE','usually_inside_paren',4,'p_usually_inside_paren','Sintatico.py',126),
  ('usually_inside_paren -> statement_property_identify statement_reserved_word NUMBER NAMESPACEID DATA_TYPE','usually_inside_paren',5,'p_usually_inside_paren','Sintatico.py',127),
  ('usually_inside_paren -> statement_property_identify statement_reserved_word NUMBER CLASS_IDENTIFIER','usually_inside_paren',4,'p_usually_inside_paren','Sintatico.py',128),
  ('usually_inside_paren -> statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET','usually_inside_paren',8,'p_usually_inside_paren','Sintatico.py',129),
  ('usually_others_paren -> statement_property_identify statement_others_reserved_word CLASS_IDENTIFIER','usually_others_paren',3,'p_usually_others_inside_paren','Sintatico.py',132),
  ('usually_others_paren -> statement_property_identify statement_others_reserved_word LEFT_PAREN usually_others_others_paren','usually_others_paren',4,'p_usually_others_inside_paren','Sintatico.py',133),
  ('usually_others_paren -> statement_property_identify statement_others_reserved_word NAMESPACEID DATA_TYPE','usually_others_paren',4,'p_usually_others_inside_paren','Sintatico.py',134),
  ('usually_others_paren -> statement_property_identify statement_others_reserved_word NUMBER NAMESPACEID DATA_TYPE','usually_others_paren',5,'p_usually_others_inside_paren','Sintatico.py',135),
  ('usually_others_paren -> statement_property_identify statement_others_reserved_word NUMBER CLASS_IDENTIFIER','usually_others_paren',4,'p_usually_others_inside_paren','Sintatico.py',136),
  ('usually_others_paren -> statement_property_identify statement_others_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET','usually_others_paren',8,'p_usually_others_inside_paren','Sintatico.py',137),
  ('usually_others_others_paren -> CLASS_IDENTIFIER RIGHT_PAREN','usually_others_others_paren',2,'p_usually_others_others_inside_paren','Sintatico.py',140),
  ('usually_others_others_paren -> CLASS_IDENTIFIER OR usually_others_others_paren','usually_others_others_paren',3,'p_usually_others_others_inside_paren','Sintatico.py',141),
  ('simple_paren -> LEFT_PAREN usually_inside_paren RIGHT_PAREN','simple_paren',3,'p_simple_paren','Sintatico.py',144),
  ('simple_other_paren -> LEFT_PAREN usually_others_paren RIGHT_PAREN','simple_other_paren',3,'p_simple_other_paren','Sintatico.py',148),
  ('expression -> usually_inside_paren','expression',1,'p_expression','Sintatico.py',153),
  ('expression -> usually_inside_paren COMMA expression','expression',3,'p_expression','Sintatico.py',154),
  ('expression -> simple_paren','expression',1,'p_expression','Sintatico.py',155),
  ('expression -> simple_paren COMMA expression','expression',3,'p_expression','Sintatico.py',156),
  ('expression -> simple_paren AND expression','expression',3,'p_expression','Sintatico.py',157),
  ('other_expression -> usually_inside_paren','other_expression',1,'p_other_expression','Sintatico.py',160),
  ('other_expression -> usually_others_paren','other_expression',1,'p_other_expression','Sintatico.py',161),
  ('other_expression -> usually_inside_paren COMMA other_expression','other_expression',3,'p_other_expression','Sintatico.py',162),
  ('other_expression -> usually_others_paren COMMA other_expression','other_expression',3,'p_other_expression','Sintatico.py',163),
  ('other_expression -> simple_other_paren','other_expression',1,'p_other_expression','Sintatico.py',164),
  ('other_expression -> simple_other_paren COMMA other_expression','other_expression',3,'p_other_expression','Sintatico.py',165),
  ('other_expression -> simple_other_paren AND other_expression','other_expression',3,'p_other_expression','Sintatico.py',166),
  ('other_expression -> usually_others_paren AND other_expression','other_expression',3,'p_other_expression','Sintatico.py',167),
  ('nested -> CLASS_IDENTIFIER AND nested_descriptions','nested',3,'p_statement_aninhada_class','Sintatico.py',172),
  ('nested -> CLASS_IDENTIFIER COMMA nested_descriptions','nested',3,'p_statement_aninhada_class','Sintatico.py',173),
  ('nested_descriptions -> nested_descriptions AND nested_descriptions','nested_descriptions',3,'p_nested_descriptions','Sintatico.py',180),
  ('nested_descriptions -> nested_descriptions OR nested_descriptions','nested_descriptions',3,'p_nested_descriptions','Sintatico.py',181),
  ('nested_descriptions -> LEFT_PAREN nested_descriptions RIGHT_PAREN','nested_descriptions',3,'p_nested_descriptions','Sintatico.py',182),
  ('nested_descriptions -> statement_property_identify statement_others_reserved_word nested_descriptions','nested_descriptions',3,'p_nested_descriptions','Sintatico.py',183),
  ('nested_descriptions -> statement_property_identify statement_others_reserved_word CLASS_IDENTIFIER','nested_descriptions',3,'p_nested_descriptions','Sintatico.py',184),
  ('nested_descriptions -> statement_property_identify statement_others_reserved_word VALUE CLASS_IDENTIFIER','nested_descriptions',4,'p_nested_descriptions','Sintatico.py',185),
  ('nested_descriptions -> statement_property_identify statement_others_reserved_word VALUE IndividualNames','nested_descriptions',4,'p_nested_descriptions','Sintatico.py',186),
  ('nested_descriptions -> statement_property_identify VALUE IndividualNames','nested_descriptions',3,'p_nested_descriptions','Sintatico.py',187),
  ('nested_descriptions -> statement_property_identify VALUE CLASS_IDENTIFIER','nested_descriptions',3,'p_nested_descriptions','Sintatico.py',188),
  ('nested_descriptions -> statement_property_identify statement_others_reserved_word VALUE nested_descriptions','nested_descriptions',4,'p_nested_descriptions','Sintatico.py',189),
  ('nested_descriptions -> statement_property_identify statement_others_reserved_word NUMBER nested_descriptions','nested_descriptions',4,'p_nested_descriptions','Sintatico.py',190),
  ('nested_descriptions -> statement_property_identify statement_others_reserved_word ONLY CLASS_IDENTIFIER','nested_descriptions',4,'p_nested_descriptions','Sintatico.py',191),
  ('nested_descriptions -> statement_property_identify statement_others_reserved_word ONLY nested_descriptions','nested_descriptions',4,'p_nested_descriptions','Sintatico.py',192),
  ('nested_descriptions -> statement_property_identify statement_others_reserved_word SOME CLASS_IDENTIFIER','nested_descriptions',4,'p_nested_descriptions','Sintatico.py',193),
  ('nested_descriptions -> statement_property_identify statement_others_reserved_word SOME nested_descriptions','nested_descriptions',4,'p_nested_descriptions','Sintatico.py',194),
  ('nested_descriptions -> CLASS_IDENTIFIER','nested_descriptions',1,'p_nested_descriptions','Sintatico.py',195),
  ('statement_closed_axiom_class -> CLASS_IDENTIFIER COMMA other_expression','statement_closed_axiom_class',3,'p_statement_closed_axiom_class','Sintatico.py',208),
  ('statement_closed_axiom_class -> CLASS_IDENTIFIER AND other_expression','statement_closed_axiom_class',3,'p_statement_closed_axiom_class','Sintatico.py',209),
  ('statement_closed_axiom_class -> CLASS_IDENTIFIER other_expression','statement_closed_axiom_class',2,'p_statement_closed_axiom_class','Sintatico.py',210),
  ('closed_axiom_restriction_combination -> CLASS_IDENTIFIER','closed_axiom_restriction_combination',1,'p_closed_axiom_restriction_combination','Sintatico.py',218),
  ('closed_axiom_restriction_combination -> CLASS_IDENTIFIER OR closed_axiom_restriction_combination','closed_axiom_restriction_combination',3,'p_closed_axiom_restriction_combination','Sintatico.py',219),
  ('statement_enumerated_class -> LEFT_CURLY_BRACKET statement_enumerated_class_check RIGHT_CURLY_BRACKET','statement_enumerated_class',3,'p_statement_enumerated_class','Sintatico.py',224),
  ('statement_enumerated_class_check -> IndividualNames','statement_enumerated_class_check',1,'p_statement_enumerated_class_check','Sintatico.py',231),
  ('statement_enumerated_class_check -> IndividualNames COMMA statement_enumerated_class_check','statement_enumerated_class_check',3,'p_statement_enumerated_class_check','Sintatico.py',232),
  ('statement_covered_class -> statement_covered_class_check','statement_covered_class',1,'p_statement_covered_class','Sintatico.py',237),
  ('statement_covered_class_check -> CLASS_IDENTIFIER','statement_covered_class_check',1,'p_statement_covered_class_check','Sintatico.py',244),
  ('statement_covered_class_check -> CLASS_IDENTIFIER OR statement_covered_class_check','statement_covered_class_check',3,'p_statement_covered_class_check','Sintatico.py',245),
  ('empty -> <empty>','empty',0,'p_empty','Sintatico.py',250),
]
