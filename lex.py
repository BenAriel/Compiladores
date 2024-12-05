import ply.lex as lex
from ply.lex import TOKEN

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
)

reserved = {
    'not': 'NOT',
    'and': 'AND',
}

def t_reserved(t):
    t.type = reserved[t.value.lower()]  # Define o tipo do token com base no dicionário
    t.lexer.num_reserved += 1
    return t


reserved_geral = r'\b([Nn][Oo][Tt]|[Aa][Nn][Dd]|[Oo][Rr]|[Ss][Oo][Mm][Ee]|[Aa][Ll][Ll]|[Vv][Aa][Ll][Uu][Ee]|[Mm][Ii][Nn]|[Mm][Aa][Xx]|[Ee][Xx][Aa][Cc][Tt][Ll][Yy]|[Tt][Hh][Aa][Tt])\b'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'


#FUNÇÕES DAS PALAVRAS RESERVADAS
def t_NOT(t):
    r'[Nn][Oo][Tt]'
    t.lexer.num_reserved+=1
    return t

def t_AND(t):
    r'[Aa][Nn][Dd]'
    t.lexer.num_reserved+=1
    return t


def t_OR(t):
    r'[Oo][Rr]'
    t.lexer.num_reserved+=1
    return t

def t_SOME(t):
    r'[Ss][Oo][Mm][Ee]'
    t.lexer.num_reserved+=1
    return t

def t_ALL(t):
    r'[Aa][Ll][Ll]'
    t.lexer.num_reserved+=1
    return t

def t_VALUE(t):
    r'[Vv][Aa][Ll][Uu][Ee]'
    t.lexer.num_reserved+=1
    return t

def t_MIN(t):
    r'[Mm][Ii][Nn]'
    t.lexer.num_reserved+=1
    return t

def t_MAX(t):
    r'[Mm][Aa][Xx]'
    t.lexer.num_reserved+=1
    return t

def t_EXACTLY(t):
    r'[Ee][Xx][Aa][Cc][Tt][Ll][Yy]'
    t.lexer.num_reserved+=1
    return t

def t_THAT(t):
    r'[Tt][Hh][Aa][Tt]'
    t.lexer.num_reserved+=1
    return t

def t_CLASS(t):
    r'Class'
    t.lexer.num_reserved=+1
    return t

def t_EQUIVALENTETO(t):
    r'EquivalentTo'
    t.lexer.num_reserved=+1
    return t






def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
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


data = data = '''
Not AND not and AnD
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