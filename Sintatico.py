import ply.yacc as yacc
from Lex import tokens  # Importa os tokens definidos no léxico

class_counter = 0
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
    
    print(f"Classe definida")
def p_statement_primitive_class(p):
    '''statement_primitive_class : subclassof_possible statement_class_disjoin statement_class_individuals'''
    print(f"Classe primitiva: {p[1]}")

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
    '''subclassof_possible : SubClassOf primitive_class_mandatory
                           | SubClassOf statement_closed_axiom_class'''
    pass

def p_justDefined(p):
    '''JustDefined :  CLASS_IDENTIFIER AND LEFT_PAREN statement_defined_class_equivalent statement_class_individuals
                        | CLASS_IDENTIFIER COMMA statement_defined_class_equivalent statement_class_individuals'''
    print(f"Classe definida normal: {p[1]}")
    pass
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


def p_nested(p):
    '''nested : nested AND nested
                           | nested OR nested
                           | LEFT_PAREN nested RIGHT_PAREN
                           | statement_property_identify statement_reserved_word nested
                           | statement_property_identify statement_reserved_word CLASS_IDENTIFIER
                           | statement_property_identify statement_reserved_word VALUE CLASS_IDENTIFIER
                           | statement_property_identify statement_reserved_word VALUE nested
                           | statement_property_identify statement_reserved_word ONLY CLASS_IDENTIFIER
                           | statement_property_identify statement_reserved_word ONLY nested
                           | statement_property_identify statement_reserved_word SOME CLASS_IDENTIFIER
                           | statement_property_identify statement_reserved_word SOME nested
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
    '''statement_closed_axiom_class : CLASS_IDENTIFIER COMMA closed_axiom_mandatory'''
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

# Classes enumeradas
def p_statement_enumerated_class(p):
    '''statement_enumerated_class : LEFT_CURLY_BRACKET statement_enumerated_class_check RIGHT_CURLY_BRACKET'''
    print(f"Classe enumerada: {p[2]}")

def p_statement_enumerated_class_check(p):
    '''statement_enumerated_class_check : IndividualNames
                                        | IndividualNames COMMA statement_enumerated_class_check'''
    pass

# Classes cobertas
def p_statement_covered_class(p):
    '''statement_covered_class : statement_covered_class_check'''
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