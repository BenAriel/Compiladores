import ply.lex as lex
from ply.lex import TOKEN

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
    'EquivalentTo',
    'Individuals',
    'SubClassOf',
    'DisjointClasses',
    'IndividualNames',
    'SpecialCharacters',
    'PROPERTY_IDENTIFIER',
    'PROPERTY_IDENTIFIER_has',
    'PROPERTY_IDENTIFIER_is_Of',
    'CLASS_IDENTIFIER',
    'owl',
    'rdf',
    'rdfs',
    'xsd',
    'rational',
    'real',
    'langString',
    'PlainLiteral',
    'XMLLiteral',
    'Literal',
    'anyURI',
    'base64Binary',
    'boolean',
    'byte',
    'dateTime',
    'dateTimeStamp',
    'decimal',
    'double',
    'float',
    'hexBinary',
    'int',
    'integer',
    'languague',
    'long',
    'Name',
    'NCName',
    'negativeInteger',
    'NMTOKEN',
    'nonNegativeInteger',
)

reserved = {
    'not': 'NOT',
    'and': 'AND',
    'or': 'OR',
    'some': 'SOME',
    'all': 'ALL',
    'value': 'VALUE',
    'min': 'MIN',
    'max': 'MAX',
    'exactly': 'EXACTLY',
    'that': 'THAT',
    'equivalentto:': 'EquivalentTo',
    'individuals:': 'Individuals',
    'subclassof:': 'SubClassOf',
    'disjointclasses:': 'DisjointClasses',
    'owl:' : 'owl',
    'rdf:' : 'rdf',
    'rdfs:' : 'rdfs',
    'xsd:' : 'xsd',
    'rational' : 'rational',
    'real' : 'real',
    'langString' : 'langString',
    'PlainLiteral' : 'PlainLiteral',
    'XMLLiteral' : 'XMLLiteral',
    'Literal' : 'Literal',
    'anyURI' : 'anyURI',
    'base64Binary' : 'base64Binary',
    'boolean' : 'boolean',
    'byte' : 'byte',
    'dateTime' : 'dateTime',
    'dateTimeStamp' : 'dateTimeStamp',
    'decimal' : 'decimal',
    'double' : 'double',
    'float' : 'float',
    'hexBinary' : 'hexBinary',
    'int' : 'int',
    'integer' : 'integer',
    'languague' : 'languague',
    'long' : 'long',
    'Name' : 'Name',
    'NCName' : 'NCName',
    'negativeInteger' : 'negativeInteger',
    'NMTOKEN' : 'NMTOKEN',
    'nonNegativeInteger' : 'nonNegativeInteger',
}

RESERVED_GERAL = r'\b([Nn][Oo][Tt]|[Aa][Nn][Dd]|[Oo][Rr]|[Ss][Oo][Mm][Ee]|[Aa][Ll][Ll]|[Vv][Aa][Ll][Uu][Ee]|[Mm][Ii][Nn]|[Mm][Aa][Xx]|[Ee][Xx][Aa][Cc][Tt][Ll][Yy]|[Tt][Hh][Aa][Tt])\b'
RESERVED_OTHERS = r'(EquivalentTo:|Individuals:|SubClassOf:|DisjointClasses:)'
INDIVIDUALS_NAMES = r'\b[A-Z][a-zA-Z]*\d+\b'
SPECIAL_CARACTERES = r'[\(\)\[\]\{\}\,\<\>\"]'
class_identifier = r'\b[A-Z][a-zA-Z]*(\s[A-Z][a-zA-Z])*\b'
property_identifier = r'\b([a-z][a-zA-Z]*|is[A-Z][a-zA-Z]*Of|has[A-Z][a-zA-Z])\b'
data_type = r'\b(owl:|rfg:|rdfs:|xsd:|rational|real|langString|PlainLiteral|XMLLiteral|Literal|anyURI|base64Binary|boolean|byte|dateTime|dateTimeStamp|decimal|double|float|hexBinary|int|integer|language|long|Name|NCName|negativeInteger|NMTOKEN|nonNegativeInteger)\b'

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
def t_NUMBER(t):
    r'\b(\d+)\b'
    t.value = int(t.value)
    t.lexer.num_numbers += 1
    return t

@TOKEN(RESERVED_GERAL)
def t_RESERVED_GERAL(t):
    t.type = reserved[t.value.lower()]
    t.lexer.num_reserved += 1
    return t

@TOKEN(RESERVED_OTHERS)
def t_RESERVED_OTHERS(t):
    t.type = reserved[t.value.lower()]
    t.lexer.num_reserved += 1
    return t

@TOKEN(data_type)
def t_DATA_TYPE(t):
    t.type = reserved[t.value.lower()] 
    if t.value == 'owl:' or t.value == 'xsd:' or t.value == 'rdfs' or t.value == 'rdf':
        t.value = 'NAMESPACEID'
    else: 
        t.value = 'DATA_TYPE'
    t.lexer.num_reserved += 1
    return t

@TOKEN(property_identifier)
def t_PROPERTY_IDENTIFIER(t):
    if t.value.startswith("has"):
        t.type = "PROPERTY_IDENTIFIER_has"
    elif t.value.startswith("is") and t.value.endswith("Of"):
        t.type = "PROPERTY_IDENTIFIER_is_Of"
    else:
        t.type = "PROPERTY_IDENTIFIER"
    t.lexer.num_reserved += 1
    return t

@TOKEN(class_identifier)
def t_CLASS_IDENTIFIER(t):
    t.lexer.num_reserved += 1
    return t

@TOKEN(INDIVIDUALS_NAMES)
def t_INDIVIDUAL_NAMES(t):
    t.lexer.num_individual_names += 1
    t.type = "IndividualNames"
    return t

@TOKEN(SPECIAL_CARACTERES)
def t_SPECIAL_CHARACTERS(t):
    t.type = "SpecialCharacters"
    t.lexer.num_special_characters += 1
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_COMMENT(t):
    r'\#.*'
    pass

def t_error(t):
    # Captura o início da sequência ilegal
    illegal_sequence = t.value[0]
    i = 1
    
    # Continua capturando enquanto os caracteres não forem reconhecidos e não forem espaços
    while i < len(t.value) and not t.value[i].isspace() and not any(t.value[i:].startswith(p) for p in ['+', '-', '*', '/', '(', ')']):
        illegal_sequence += t.value[i]
        i += 1
    
    # Reporta a sequência inteira como um erro
    print(f"Illegal sequence: '{illegal_sequence}' at line {t.lineno}")
    
    # Avança o lexer pelo tamanho da sequência ilegal
    t.lexer.skip(len(illegal_sequence))


# Build the lexer
lexer = lex.lex(debug=True)
lexer.num_reserved = 0
lexer.num_individual_names = 0
lexer.num_special_characters = 0
lexer.num_numbers = 0

# Reading data from a file
file_path = 'input.txt'
with open(file_path, 'r') as file:
    data = file.read()

lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

print("Number of Reserved Words:", lexer.num_reserved)
print("Number of Individual Names:", lexer.num_individual_names)
print("Number of Special Characters:", lexer.num_special_characters)
print("Number of Numbers:", lexer.num_numbers)
