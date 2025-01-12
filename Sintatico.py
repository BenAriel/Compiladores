import ply.yacc as yacc
from Lex import tokens  # Importa os tokens definidos no léxico

# Regras de produção1


def p_statement_primitive_class(p): #Apenas some ou todas palavras reservadas?
    '''statement : Class CLASS_IDENTIFIER subClassOf primitive_class_mandatory statement_class_disjoin statement_class_individuals '''
    print(f"Classe primitiva: {p[2]}")
def primitive_class_mandatory(p):
    '''primitive_class_alternatives : PROPERTY_IDENTIFIER_has  SOME CLASS_IDENTIFIER    
    | PROPERTY_IDENTIFIER_has  SOME CLASS_IDENTIFIER SpecialCharacters primitive_class_alternatives
    | PROPERTY_IDENTIFIER_has  SOME NAMESPACEID DATA_TYPE
    | PROPERTY_IDENTIFIER_has  SOME NAMESPACEID DATA_TYPE SpecialCharacters primitive_class_alternatives

    ''' 

def statement_class_disjoin(p):
    '''
    statement_class_disjoin : empty
    | DisjointClasses statement_class_disjoin_check''' 


def p_statement_class_disjoin_check(p):
    '''statement_class_disjoin_check : CLASS_IDENTIFIER
    | CLASS_IDENTIFIER SpecialCharacters statement_class_disjoin_check'''

def statement_class_individuals(p):
    '''
    statement_class_individuals : empty
    | Individuals statement_class_individuals_check''' 


def p_statement_class_individuals_check(p):
    '''statement_class_individuals_check : IndividualNames
    | IndividualNames SpecialCharacters statement_class_disjoin_check'''

def p_statement_property(p):
    '''statement : PROPERTY_IDENTIFIER CLASS_IDENTIFIER'''
    print(f"Propriedade: {p[1]} para classe {p[2]}")

def p_statement_subclass_property(p):
    '''statement : SubClassOf PROPERTY_IDENTIFIER CLASS_IDENTIFIER'''
    print(f"Subclasse de {p[2]} com propriedade {p[3]}")

def p_statement_and(p):
    '''statement : CLASS_IDENTIFIER AND CLASS_IDENTIFIER'''
    print(f"Classes combinadas: {p[1]} and {p[3]}")

def p_statement_with_comma(p):
    '''statement : CLASS_IDENTIFIER SpecialCharacters CLASS_IDENTIFIER'''
    print(f"Classes separadas por vírgula: {p[1]} , {p[3]}")
    

def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: Token inesperado '{p.value}'")
    else:
        print("Erro de sintaxe: fim inesperado de entrada.")

def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: Token inesperado '{p.value}'")
    else:
        print("Erro de sintaxe: fim inesperado do arquivo.")

# Cria o parser
parser = yacc.yacc()
