import ply.lex as lex
from ply.lex import TOKEN
import re
# List of token names.   This is always required
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
   'EquivalenteTo',
   'Individuals',
   'SubClassOf',
   'DisjointClasses',
   'IndividualNames',
)

reserved = {
    'not': 'NOT', 
    'and': 'AND',
    'NOT' : 'NOT',
    'or': 'OR',
    'some': 'SOME',
    'all': 'ALL',
    'value': 'VALUE',
    'min': 'MIN',
    'max': 'MAX',
    'exactly': 'EXACTLY',
    'that': 'THAT',
    'class': 'Class',
    'equivalenteto' : 'EquivalenteTo',
    'individuals' : 'Individuals',
    'subclassof' : 'SubClassOf',
    'disjointclasses': 'DisjointClasses', 
}


RESERVED_GERAL = r'\b([Nn][Oo][Tt]|[Aa][Nn][Dd]|[Oo][Rr]|[Ss][Oo][Mm][Ee]|[Aa][Ll][Ll]|[Vv][Aa][Ll][Uu][Ee]|[Mm][Ii][Nn]|[Mm][Aa][Xx]|[Ee][Xx][Aa][Cc][Tt][Ll][Yy]|[Tt][Hh][Aa][Tt])\b'
RESERVED_OTHERS = r'\b(EquivalenteTo|Individuals|SubClassOf|DisjointClasses)\b'
INDIVIDUALS_NAMES = r'\b[A-Z][a-z].*\d\b'

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'


#FUNÇÕES DAS PALAVRAS RESERVADAS
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
    t.type="IndividualNames"
    return t




def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'


def t_COMMENT(t):
    r'\#.*'
    pass

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex(debug=True)
lexer.num_reserved = 0
lexer.num_individual_names=0


data = '''
AAAAAAAAAAAriel12FDFDFDFD     12ARIEL
BenAriel12
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

print(lexer.num_reserved)
print(lexer.num_individual_names)