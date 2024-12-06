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
}


RESERVED_GERAL = r'\b([Nn][Oo][Tt]|[Aa][Nn][Dd]|[Oo][Rr]|[Ss][Oo][Mm][Ee]|[Aa][Ll][Ll]|[Vv][Aa][Ll][Uu][Ee]|[Mm][Ii][Nn]|[Mm][Aa][Xx]|[Ee][Xx][Aa][Cc][Tt][Ll][Yy]|[Tt][Hh][Aa][Tt])\b'
RESERVED_OTHERS = r'(EquivalentTo:|Individuals:|SubClassOf:|DisjointClasses:)'
INDIVIDUALS_NAMES = r'\b[A-Z][a-zA-Z]*\d+\b'
SPECIAL_CARACTERES = r'[\(\)\[\]\{\}\,\<\>\"]'

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
def t_NUMBER(t):
    r'\b(\d+)\b'
    t.value = int(t.value)
    t.lexer.num_numbers+=1
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
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex(debug=True)
lexer.num_reserved = 0
lexer.num_individual_names = 0
lexer.num_special_characters = 0
lexer.num_numbers=0

data = '''
{AAAAAAAAAAAriel12FDFDFDFD    Ariel12 12ARIEL
<BenAriel}12>  ["5"] aaaaaEquivalentTo:aaa Individuals: SubClassOf: DisjointClasses:
'''


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
