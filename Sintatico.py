import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens que você já definiu
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'NOT',
    'AND',
    'OR',
    'SOME',
    'ALL',
    'VALUE',
    'MIN',
    'MAX',
    'EXACTLY',
    'THAT',
    'Class',
    'EquivalentTo',
    'Individuals',
    'SubClassOf',
    'DisjointClasses',
    'PROPERTY_IDENTIFIER',
    'PROPERTY_IDENTIFIER_has',
    'PROPERTY_IDENTIFIER_is_Of',
    'CLASS_IDENTIFIER',
    'NAMESPACEID',
    'IndividualNames',
    'SpecialCharacters',  # Adicionei aqui o token SpecialCharacters
)

# Definindo as expressões regulares para os tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NOT = r'not'
t_AND = r'and'
t_OR = r'or'
t_SOME = r'some'
t_ALL = r'all'
t_VALUE = r'value'
t_MIN = r'min'
t_MAX = r'max'
t_EXACTLY = r'exactly'
t_THAT = r'that'
t_CLASS_IDENTIFIER = r'[A-Z][a-zA-Z_]*'
t_PROPERTY_IDENTIFIER = r'[a-z][a-zA-Z_]*'
t_PROPERTY_IDENTIFIER_has = r'has[a-zA-Z_]*'
t_PROPERTY_IDENTIFIER_is_Of = r'is[a-zA-Z_]*Of'
t_NAMESPACEID = r'[a-zA-Z]{3,4}:'
t_IndividualNames = r'[A-Z][a-zA-Z]*\d+'
t_SpecialCharacters = r'[\[\]\{\}\(\)\,\<\>]'

# Definindo o token para números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Convertendo para inteiro
    return t

# Ignorando espaços em branco e novas linhas
t_ignore = ' \t\n'

# Função para lidar com erros léxicos
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Criando o lexer
lexer = lex.lex()

# Definindo as regras da gramática para o parser
precedence = (
    ('left', 'OR', 'AND'),
    ('left', 'NOT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'),
)

# Definição da gramática
def p_expression_binop(p):
    '''expression : expression AND expression
                  | expression OR expression'''
    if p[2] == 'and':
        p[0] = ('AND', p[1], p[3])
    elif p[2] == 'or':
        p[0] = ('OR', p[1], p[3])

def p_expression_not(p):
    '''expression : NOT expression'''
    p[0] = ('NOT', p[2])

def p_expression_value(p):
    '''expression : VALUE'''
    p[0] = ('VALUE', p[1])

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = ('NUMBER', p[1])

def p_expression_comparison(p):
    '''expression : CLASS_IDENTIFIER MIN expression
                  | CLASS_IDENTIFIER MAX expression
                  | CLASS_IDENTIFIER EXACTLY expression
                  | CLASS_IDENTIFIER VALUE'''
    p[0] = ('COMPARISON', p[1], p[2], p[3])

def p_expression_class(p):
    '''expression : CLASS_IDENTIFIER'''
    p[0] = ('CLASS', p[1])

def p_expression_property(p):
    '''expression : PROPERTY_IDENTIFIER'''
    p[0] = ('PROPERTY', p[1])

def p_expression_namespace(p):
    '''expression : NAMESPACEID'''
    p[0] = ('NAMESPACE', p[1])

def p_expression_individual(p):
    '''expression : IndividualNames'''
    p[0] = ('INDIVIDUAL', p[1])

def p_expression_cardinality(p):
    '''expression : PROPERTY_IDENTIFIER MIN NUMBER
                  | PROPERTY_IDENTIFIER MAX NUMBER
                  | PROPERTY_IDENTIFIER EXACTLY NUMBER'''
    p[0] = ('CARDINALITY', p[1], p[2], p[3])

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

# Erro de sintaxe
def p_error(p):
    print("Erro de sintaxe em:", p)

# Construção do parser
parser = yacc.yacc()

# Função para analisar o código
def parse(data):
    return parser.parse(data, lexer=lexer)

# Testando o parser
if __name__ == '__main__':
    # lendo o arquivo de entrada
    file_path = 'input.txt'
    with open(file_path, 'r') as file:
        data = file.read()

    lexer.input(data)
    result = parse(data)
    print(result)
