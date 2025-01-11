import ply.yacc as yacc
from Lex import tokens  # Importa os tokens do seu lexer

# Estrutura para armazenar os elementos do OWL
owl_structure = {
    "Classes": {},
    "Individuals": {},
    "DisjointClasses": [],
    "Properties": {},
}

# Regras de gramática
def p_ontology(p):
    '''ontology : statements'''
    p[0] = p[1]

def p_statements_multiple(p):
    '''statements : statements statement'''
    p[0] = p[1]
    p[0].append(p[2])

def p_statements_single(p):
    '''statements : statement'''
    p[0] = [p[1]]

def p_statement_class(p):
    '''statement : Class CLASS_IDENTIFIER properties'''
    owl_structure["Classes"][p[2]] = p[3]

def p_statement_individuals(p):
    '''statement : Individuals ':' individual_list'''
    owl_structure["Individuals"] = p[3]

def p_statement_disjointclasses(p):
    '''statement : DisjointClasses ':' class_list'''
    owl_structure["DisjointClasses"] = p[3]

def p_properties(p):
    '''properties : EquivalentTo ':' class_list
                  | SubClassOf ':' class_list
                  | empty'''
    if len(p) > 2:
        p[0] = {p[1]: p[3]}
    else:
        p[0] = {}

def p_individual_list(p):
    '''individual_list : individual_list ',' IndividualNames
                       | IndividualNames'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_class_list(p):
    '''class_list : class_list ',' CLASS_IDENTIFIER
                  | CLASS_IDENTIFIER'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_empty(p):
    '''empty :'''
    pass

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

result = parser.parse(data)
print("\n=== Estrutura OWL ===")
print(owl_structure)
