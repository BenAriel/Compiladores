import ply.yacc as yacc
from Lex import tokens  # Importa os tokens definidos no léxico

# Conjunto inicial de regras de produção
def p_statements(p):
    '''statements : statement
                  | statement statements'''
    pass

# Classes primitivas
def p_statement_primitive_class(p):
    '''statement : Class CLASS_IDENTIFIER SubClassOf primitive_class_mandatory statement_class_disjoin statement_class_individuals'''
    print(f"Classe primitiva: {p[2]}")

def p_statement_reserved_word(p):
    '''statement_reserved_word : SOME
                               | EXACTLY
                               | MIN
                               | MAX
                               | OR
                               | ONLY
                               | AND
                               | VALUE'''
    p[0] = p[1]

def p_statement_property_identify(p):
    '''statement_property_identify : PROPERTY_IDENTIFIER_has
                                   | PROPERTY_IDENTIFIER_is_Of
                                   | PROPERTY_IDENTIFIER'''
    p[0] = p[1]

def p_primitive_class_mandatory(p):
    '''primitive_class_mandatory : statement_property_identify statement_reserved_word CLASS_IDENTIFIER
                                 | statement_property_identify statement_reserved_word CLASS_IDENTIFIER COMMA primitive_class_mandatory
                                 | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE
                                 | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE COMMA primitive_class_mandatory
                                 | CLASS_IDENTIFIER
                                 | CLASS_IDENTIFIER COMMA primitive_class_mandatory'''
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

# funções para classe definida
def p_statement_defined_class(p):
    '''statement : Class CLASS_IDENTIFIER EquivalentTo CLASS_IDENTIFIER AND LEFT_PAREN statement_defined_class_equivalent statement_class_individuals'''
    print(f"Classe definida: {p[2]}") 
    return p[2]

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
                                 | GREATER_THAN EQUALS
                                 | LESS_THAN EQUALS'''
    pass

# Classes com axiomas fechados
def p_statement_closed_axiom_class(p):
    '''statement : Class CLASS_IDENTIFIER SubClassOf CLASS_IDENTIFIER COMMA closed_axiom_mandatory'''
    print(f"Classe axioma fechada: {p[2]}")

def p_closed_axiom_mandatory(p):
    '''closed_axiom_mandatory : CLASS_IDENTIFIER
                              | statement_property_restriction
                              | CLASS_IDENTIFIER COMMA closed_axiom_mandatory
                              | statement_property_restriction COMMA closed_axiom_mandatory'''
    pass

def p_statement_property_restriction(p):
    '''statement_property_restriction : statement_property_identify SOME CLASS_IDENTIFIER
                                      | statement_property_identify ONLY LEFT_PAREN closed_axiom_restriction_combination RIGHT_PAREN'''
    pass

def p_closed_axiom_restriction_combination(p):
    '''closed_axiom_restriction_combination : CLASS_IDENTIFIER
                                            | CLASS_IDENTIFIER OR closed_axiom_restriction_combination'''
    pass

# Classes com descrições aninhadas
def p_statement_nested_descriptions_class(p):
    '''statement : Class CLASS_IDENTIFIER EquivalentTo CLASS_IDENTIFIER AND LEFT_PAREN nested_descriptions RIGHT_PAREN'''
    print(f"Classe com descrições aninhadas: {p[2]}")

def p_nested_descriptions(p):
    '''nested_descriptions : nested_descriptions OR nested_descriptions
                          | nested_descriptions AND nested_descriptions
                          | LEFT_PAREN nested_descriptions RIGHT_PAREN
                          | statement_property_identify statement_reserved_word CLASS_IDENTIFIER
                          | statement_property_identify statement_reserved_word nested_descriptions
                          | statement_property_identify statement_reserved_word VALUE CLASS_IDENTIFIER
                          | statement_property_identify statement_reserved_word VALUE nested_descriptions
                          | statement_property_identify statement_reserved_word ONLY CLASS_IDENTIFIER
                          | statement_property_identify statement_reserved_word ONLY nested_descriptions
                          | statement_property_identify statement_reserved_word SOME CLASS_IDENTIFIER
                          | statement_property_identify statement_reserved_word SOME nested_descriptions
                          | CLASS_IDENTIFIER'''
    pass
    
# Classes enumeradas
def p_statement_enumerated_class(p):
    '''statement : Class CLASS_IDENTIFIER EquivalentTo LEFT_CURLY_BRACKET statement_enumerated_class_check RIGHT_CURLY_BRACKET'''
    print(f"Classe enumerada: {p[2]}")

def p_statement_enumerated_class_check(p):
    '''statement_enumerated_class_check : IndividualNames
                                        | IndividualNames COMMA statement_enumerated_class_check'''
    pass

# Classes cobertas
def p_statement_covered_class(p):
    '''statement : Class CLASS_IDENTIFIER EquivalentTo statement_covered_class_check'''
    print(f"Classe coberta: {p[2]}")

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