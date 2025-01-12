import ply.yacc as yacc
from Lex import lexer
from Lex import tokens

# Função para imprimir os tokens conforme o lexer os processa
def imprimir_tokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f"Token: {tok.type} - Valor: {tok.value}")

# Regra de classes primitivas
def p_statement_class_primitive(p):
    '''statement : Class CLASS_IDENTIFIER SubClassOf properties DisjointClasses IndividualNames'''
    class_name = p[2]
    properties = p[4]
    disjoint_classes = p[5]
    individuals = p[6]
    
    print(f"Classe Primitiva: {class_name}")
    print(f"Propriedades: {properties}")
    print(f"DisjointClasses: {disjoint_classes}")
    print(f"Indivíduos: {individuals}")

# Regra de classes definidas
def p_statement_class_defined(p):
    '''statement : Class CLASS_IDENTIFIER EquivalentTo conditions IndividualNames'''
    class_name = p[2]
    conditions = p[4]
    individuals = p[5]
    
    print(f"Classe Definida: {class_name}")
    print(f"Condições: {conditions}")
    print(f"Indivíduos: {individuals}")

# Regra de classes com fechamento
def p_statement_class_closure(p):
    '''statement : Class CLASS_IDENTIFIER SubClassOf properties DisjointClasses IndividualNames Closure restrictions'''
    class_name = p[2]
    properties = p[4]
    disjoint_classes = p[5]
    individuals = p[6]
    closure = p[7]  # Regras de fechamento
    
    print(f"Classe com Fechamento: {class_name}")
    print(f"Propriedades: {properties}")
    print(f"DisjointClasses: {disjoint_classes}")
    print(f"Indivíduos: {individuals}")
    print(f"Fechamento: {closure}")

# Regra de classes aninhadas
def p_statement_class_nested(p):
    '''statement : Class CLASS_IDENTIFIER EquivalentTo nested_conditions IndividualNames'''
    class_name = p[2]
    nested_conditions = p[4]
    individuals = p[5]
    
    print(f"Classe Aninhada: {class_name}")
    print(f"Condições Aninhadas: {nested_conditions}")
    print(f"Indivíduos: {individuals}")

# Regra de classes enumeradas
def p_statement_class_enumerated(p):
    '''statement : Class CLASS_IDENTIFIER EquivalentTo enumerated_instances IndividualNames'''
    class_name = p[2]
    enumerated_instances = p[4]
    individuals = p[5]
    
    print(f"Classe Enumerada: {class_name}")
    print(f"Instâncias Enumeradas: {enumerated_instances}")
    print(f"Indivíduos: {individuals}")

# Regra de classes cobertas
def p_statement_class_covered(p):
    '''statement : Class CLASS_IDENTIFIER EquivalentTo covered_classes IndividualNames'''
    class_name = p[2]
    covered_classes = p[4]
    individuals = p[5]
    
    print(f"Classe Coberta: {class_name}")
    print(f"Classes Filhas: {covered_classes}")
    print(f"Indivíduos: {individuals}")

# Definição de propriedades
def p_properties(p):
    '''properties : PROPERTY_IDENTIFIER'''
    p[0] = p[1]

# Definição de condições
def p_conditions(p):
    '''conditions : CONDITION_EXPRESSION'''
    p[0] = p[1]

# Definição de aninhamentos de condições
def p_nested_conditions(p):
    '''nested_conditions : NESTED_CONDITION_EXPRESSION'''
    p[0] = p[1]

# Instâncias enumeradas
def p_enumerated_instances(p):
    '''enumerated_instances : ENUMERATED_INSTANCE'''
    p[0] = p[1]

# Definição de classes cobertas
def p_covered_classes(p):
    '''covered_classes : COVERED_CLASS'''
    p[0] = p[1]

# Tratamento de erros
def p_error(p):
    if p:
        print(f"Erro de sintaxe próximo ao token {p.value} na linha {p.lineno}.")
    else:
        print("Erro de sintaxe no final da entrada.")

# Construção do parser
parser = yacc.yacc()

# Testando com entrada
file_path = 'input.txt'
with open(file_path, 'r') as file:
    data = file.read()

lexer.input(data)

# Imprimir todos os tokens
print("Tokens identificados:")
imprimir_tokens(lexer)

# Parse da entrada
parser.parse(data, lexer=lexer)
