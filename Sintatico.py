import ply.yacc as yacc
from Lex import tokens  # Importa os tokens definidos no léxico

# Regras de produção

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
