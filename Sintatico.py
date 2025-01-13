import ply.yacc as yacc
from Lex import tokens  # Importa os tokens definidos no léxico

# Regras de produção1

# funções para classe primitiva
def p_statement_primitive_class(p): #Apenas some ou todas palavras reservadas?
    '''statement : Class CLASS_IDENTIFIER SubClassOf primitive_class_mandatory statement_class_disjoin statement_class_individuals '''
    print(f"Classe primitiva: {p[2]}")

def p_statement_reserved_word(p):
    '''statement_reserved_word : SOME
     | EXACTLY
     | MIN
     | MAX'''
    
def p_statement_property_identify(p):
    '''statement_property_identify : PROPERTY_IDENTIFIER_has
     | PROPERTY_IDENTIFIER_is_Of
     | PROPERTY_IDENTIFIER'''
    
def p_primitive_class_mandatory(p):
    '''primitive_class_mandatory : statement_property_identify  statement_reserved_word CLASS_IDENTIFIER    
    | statement_property_identify  statement_reserved_word CLASS_IDENTIFIER SpecialCharacters primitive_class_mandatory
    | statement_property_identify  statement_reserved_word NAMESPACEID DATA_TYPE
    | statement_property_identify  statement_reserved_word NAMESPACEID DATA_TYPE SpecialCharacters primitive_class_mandatory
    | CLASS_IDENTIFIER
    | CLASS_IDENTIFIER SpecialCharacters primitive_class_mandatory
    ''' 

def p_statement_class_disjoin(p):
    '''
    statement_class_disjoin : empty
    | DisjointClasses statement_class_disjoin_check''' 


def p_statement_class_disjoin_check(p):
    '''statement_class_disjoin_check : CLASS_IDENTIFIER
    | CLASS_IDENTIFIER SpecialCharacters statement_class_disjoin_check'''

def p_statement_class_individuals(p):
    '''
    statement_class_individuals : empty
    | Individuals statement_class_individuals_check
    '''



def p_statement_class_individuals_check(p):
    '''statement_class_individuals_check : IndividualNames
    | IndividualNames SpecialCharacters statement_class_individuals_check'''

# funções para classe definida
def p_statement_defined_class(p): #todas precisam de individuos? ou é opcional?
    '''statement : Class CLASS_IDENTIFIER statement_defined_class_equivalent statement_class_individuals'''

def p_statement_defined_class_equivalent(p): #precisa de 2 versções,um com 3 caracteres especiais e outro com 2, pois pode ser por exemplo <= ou = 
    '''statement_defined_class_equivalent : EquivalentTo CLASS_IDENTIFIER AND SpecialCharacters CLASS_IDENTIFIER SOME CLASS_IDENTIFIER SpecialCharacters
    | EquivalentTo CLASS_IDENTIFIER AND SpecialCharacters CLASS_IDENTIFIER SOME NAMESPACEID DATA_TYPE SpecialCharacters SpecialCharacters SpecialCharacters NUMBER SpecialCharacters SpecialCharacters
    | EquivalentTo CLASS_IDENTIFIER AND SpecialCharacters CLASS_IDENTIFIER SOME NAMESPACEID DATA_TYPE SpecialCharacters SpecialCharacters NUMBER SpecialCharacters SpecialCharacters'''
#classe anxioma fechada

#classe enumerada
def p_statement_enumerated_class(p):
    '''statement : Class CLASS_IDENTIFIER SpecialCharacters  statement_enumerated_class_check'''


def p_statement_enumerated_class_check(p):
    '''statement_enumerated_class_check :  CLASS_IDENTIFIER 
    | CLASS_IDENTIFIER SpecialCharacters statement_enumerated_class_check'''

#classe coberta
def p_statement_covered_class(p):
    '''statement : Class CLASS_IDENTIFIER EquivalentTo statement_covered_class_check'''

def p_statement_covered_class_check(p):
    '''statement_covered_class_check : CLASS_IDENTIFIER
    | CLASS_IDENTIFIER OR statement_covered_class_check'''


def p_empty(p):
    'empty :'
    pass

    

def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: Token inesperado '{p.type}'")
    else:
        print("Erro de sintaxe: fim inesperado de entrada.")


# Cria o parser
parser = yacc.yacc()
