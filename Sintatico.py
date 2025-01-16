import ply.yacc as yacc
from Lex import tokens  # Importa os tokens definidos no léxico

# Conjunto inicial de regras de produção

def p_statements(p):
    '''statements : Class CLASS_IDENTIFIER statement_defined_class statements
                  | Class CLASS_IDENTIFIER statement_defined_class
                  | Class CLASS_IDENTIFIER statement_primitive_class
                  | Class CLASS_IDENTIFIER statement_primitive_class statements
                  | empty'''
    pass

def p_statement_defined_class(p):
    '''statement_defined_class : EquivalentTo_possible maybe_suclassof statement_class_disjoin statement_class_individuals
                               | subclassof_possible EquivalentTo_possible statement_class_disjoin statement_class_individuals'''  
    
def p_statement_primitive_class(p):
    '''statement_primitive_class : subclassof_possible statement_class_disjoin statement_class_individuals'''
    print(f"Classe primitiva: {p[-1]}")

def p_EquivalentTo_possible(p):
    '''EquivalentTo_possible : EquivalentTo JustDefined
                             | EquivalentTo nested
                             | EquivalentTo statement_closed_axiom_class
                             | EquivalentTo statement_enumerated_class
                             | EquivalentTo statement_covered_class'''
    pass

def p_maybe_suclassof(p):
    '''maybe_suclassof : subclassof_possible
                       | empty'''
    pass

def p_subclassof_possible(p):
    '''subclassof_possible : SubClassOf statement_closed_axiom_class
                           | SubClassOf statement_enumerated_class
                           | SubClassOf statement_covered_class
                           | SubClassOf primitive_class_mandatory '''
    pass

def p_justDefined(p):
    '''JustDefined : CLASS_IDENTIFIER COMMA expression statement_class_disjoin statement_class_individuals
    | CLASS_IDENTIFIER AND expression statement_class_disjoin statement_class_individuals
    | expression statement_class_disjoin statement_class_individuals'''
    print(f"Classe definida normal: {p[-2]}")
    pass

def p_statement_reserved_word(p):
    '''statement_reserved_word : SOME
                               | EXACTLY
                               | MIN
                               | MAX
                               | OR
                               | AND
                               | VALUE'''
    p[0] = p[1]

def p_statement_others_reserved_word(p):
    '''statement_others_reserved_word : SOME
                               | ONLY
                               | OR
                               | AND'''
    p[0] = p[1]

def p_statement_property_identify(p):
    '''statement_property_identify : PROPERTY_IDENTIFIER_has
                                   | PROPERTY_IDENTIFIER_is_Of
                                   | PROPERTY_IDENTIFIER'''
    p[0] = p[1]

def p_primitive_class_mandatory(p):
    '''primitive_class_mandatory : CLASS_IDENTIFIER COMMA expression statement_class_disjoin statement_class_individuals
                                 | CLASS_IDENTIFIER AND expression statement_class_disjoin statement_class_individuals
                                 | expression statement_class_disjoin statement_class_individuals
                                 | CLASS_IDENTIFIER
                                    '''
    pass

def p_statement_class_disjoin(p):
    '''statement_class_disjoin : empty
                               | DisjointClasses statement_class_disjoin_check'''
    pass

def p_statement_class_disjoin_check(p):
    '''statement_class_disjoin_check : CLASS_IDENTIFIER
                                     | CLASS_IDENTIFIER COMMA statement_class_disjoin_check'''
    pass

def p_statement_class_individuals(p):
    '''statement_class_individuals : empty
                                   | Individuals statement_class_individuals_check'''
    pass

def p_statement_class_individuals_check(p):
    '''statement_class_individuals_check : IndividualNames
                                         | IndividualNames COMMA statement_class_individuals_check'''
    pass


def p_statement_defined_class_equivalent(p):
    '''statement_defined_class_equivalent : statement_property_identify statement_reserved_word CLASS_IDENTIFIER RIGHT_PAREN
    | statement_property_identify statement_reserved_word CLASS_IDENTIFIER RIGHT_PAREN COMMA statement_defined_class_equivalent
                                          | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET RIGHT_PAREN
                                          | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET RIGHT_PAREN COMMA statement_defined_class_equivalent '''
    pass

def p_statement_operator_symbol(p):
    '''statement_operator_symbol : LESS_THAN
    | GREATER_THAN
    | EQUALS
    |  GREATER_THAN EQUALS
    | LESS_THAN EQUALS'''
    pass


def p_usually_inside_paren(p):
    '''usually_inside_paren : statement_property_identify statement_reserved_word CLASS_IDENTIFIER
    | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE
    | statement_property_identify statement_reserved_word NUMBER NAMESPACEID DATA_TYPE
    | statement_property_identify statement_reserved_word NUMBER CLASS_IDENTIFIER
    | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET'''

def p_usually_others_inside_paren(p):
    '''usually_others_paren : statement_property_identify statement_others_reserved_word CLASS_IDENTIFIER
    | statement_property_identify statement_others_reserved_word LEFT_PAREN usually_others_others_paren
    | statement_property_identify statement_others_reserved_word NAMESPACEID DATA_TYPE
    | statement_property_identify statement_others_reserved_word NUMBER NAMESPACEID DATA_TYPE
    | statement_property_identify statement_others_reserved_word NUMBER CLASS_IDENTIFIER
    | statement_property_identify statement_others_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET'''

def p_usually_others_others_inside_paren(p):
    ''' usually_others_others_paren : CLASS_IDENTIFIER RIGHT_PAREN
                                    | CLASS_IDENTIFIER OR usually_others_others_paren'''

def p_simple_paren(p):
    '''simple_paren : LEFT_PAREN usually_inside_paren RIGHT_PAREN'''
    pass


def p_expression(p):
    '''expression : usually_inside_paren
                    | usually_others_paren
                            | usually_inside_paren COMMA expression
                            | simple_paren
                            | simple_paren AND expression'''

def p_statement_class_disjoin(p):
    '''statement_class_disjoin : empty
                               | DisjointClasses statement_class_disjoin_check'''
    pass

def p_statement_class_disjoin_check(p):
    '''statement_class_disjoin_check : CLASS_IDENTIFIER
                                     | CLASS_IDENTIFIER COMMA statement_class_disjoin_check'''
    pass

def p_statement_class_individuals(p):
    '''statement_class_individuals : empty
                                   | Individuals statement_class_individuals_check'''
    pass

def p_statement_class_individuals_check(p):
    '''statement_class_individuals_check : IndividualNames
                                         | IndividualNames COMMA statement_class_individuals_check'''
    pass
    
# Classes aninhadas
def p_statement_aninhada_class(p):
    '''nested : CLASS_IDENTIFIER AND nested_descriptions
                |  CLASS_IDENTIFIER COMMA nested_descriptions'''
    print(f"Classe aninhada: {p[-2]}")

def p_nested_descriptions(p):
    '''nested_descriptions : nested_descriptions AND nested_descriptions
                           | nested_descriptions OR nested_descriptions
                           | LEFT_PAREN nested_descriptions RIGHT_PAREN
                           | statement_property_identify statement_others_reserved_word nested_descriptions
                           | statement_property_identify statement_others_reserved_word CLASS_IDENTIFIER
                           | statement_property_identify statement_others_reserved_word VALUE CLASS_IDENTIFIER
                           | statement_property_identify statement_others_reserved_word VALUE IndividualNames
                           | statement_property_identify VALUE IndividualNames
                           | statement_property_identify VALUE CLASS_IDENTIFIER
                           | statement_property_identify statement_others_reserved_word VALUE nested_descriptions
                           | statement_property_identify statement_others_reserved_word ONLY CLASS_IDENTIFIER
                           | statement_property_identify statement_others_reserved_word ONLY nested_descriptions
                           | statement_property_identify statement_others_reserved_word SOME CLASS_IDENTIFIER
                           | statement_property_identify statement_others_reserved_word SOME nested_descriptions
                           | CLASS_IDENTIFIER'''
    if len(p) == 4:
        if p[2] in ["AND", "OR"]:
            p[0] = f"({p[1]} {p[2]} {p[3]})"
        else:
            p[0] = f"{p[1]} {p[2]} {p[3]}"
    elif len(p) == 3:
        p[0] = f"({p[2]})"
    else:
        p[0] = f"{p[1]}"

# Classes com axiomas fechados
def p_statement_closed_axiom_class(p):
    '''statement_closed_axiom_class : CLASS_IDENTIFIER COMMA expression statement_property_identify ONLY LEFT_PAREN closed_axiom_restriction_combination RIGHT_PAREN
                |  CLASS_IDENTIFIER AND expression statement_property_identify ONLY LEFT_PAREN closed_axiom_restriction_combination RIGHT_PAREN
                |  CLASS_IDENTIFIER expression statement_property_identify ONLY LEFT_PAREN closed_axiom_restriction_combination RIGHT_PAREN'''
    print(f"Classe axioma fechada: {p[-2]}")

def p_closed_axiom_restriction_combination(p):
    '''closed_axiom_restriction_combination : CLASS_IDENTIFIER
                                            | CLASS_IDENTIFIER OR closed_axiom_restriction_combination'''
    pass

# Classes enumeradas
def p_statement_enumerated_class(p):
    '''statement_enumerated_class : LEFT_CURLY_BRACKET statement_enumerated_class_check RIGHT_CURLY_BRACKET'''
    print(f"Classe enumerada: {p[-2]}")

def p_statement_enumerated_class_check(p):
    '''statement_enumerated_class_check : IndividualNames
                                        | IndividualNames COMMA statement_enumerated_class_check'''
    pass

# Classes cobertas
def p_statement_covered_class(p):
    '''statement_covered_class : statement_covered_class_check'''
    print(f"Classe coberta: {p[-2]}")

def p_statement_covered_class_check(p):
    '''statement_covered_class_check : CLASS_IDENTIFIER
                                     | CLASS_IDENTIFIER OR statement_covered_class_check'''
    pass

# Produção vazia
def p_empty(p):
    'empty :'
    pass

# Tratamento de erros
def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: Token inesperado '{p.type}'")
    else:
        print("Erro de sintaxe: fim inesperado de entrada.")

# Criar o parser
parser = yacc.yacc()