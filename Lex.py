import ply.lex as lex
from ply.lex import TOKEN

# lista de tokens
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
    'string',
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
    'NAMESPACEID',
    'DATA_TYPE',
    'DisjointWith',
)
#dicionário de palavras reservadas
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
    'class:': 'Class',
    'equivalentto:': 'EquivalentTo',
    'individuals:': 'Individuals',
    'subclassof:': 'SubClassOf',
    'disjointclasses:': 'DisjointClasses',
    'disjointwith:' : 'DisjointWith',
}
#dicionário de namespaces e tipos de dados
namespacesAndTypes= {
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
    'string' : 'string',
    'languague' : 'languague',
    'long' : 'long',
    'Name' : 'Name',
    'NCName' : 'NCName',
    'negativeInteger' : 'negativeInteger',
    'NMTOKEN' : 'NMTOKEN',
    'nonNegativeInteger' : 'nonNegativeInteger',
}
# expressçao regular para palavras reservadas que podem ter variações de maiusculas e minusculas,como por exemplo: not, Not, NOT, nOt.
RESERVED_GERAL = r'\b([Nn][Oo][Tt]|[Aa][Nn][Dd]|[Oo][Rr]|[Ss][Oo][Mm][Ee]|[Aa][Ll][Ll]|[Vv][Aa][Ll][Uu][Ee]|[Mm][Ii][Nn]|[Mm][Aa][Xx]|[Ee][Xx][Aa][Cc][Tt][Ll][Yy]|[Tt][Hh][Aa][Tt])\b'

# expressão regular para palavras reservadas que não tem variacão,tem apenas uma forma de escrever.
RESERVED_OTHERS = r'(Class:|EquivalentTo:|Individuals:|SubClassOf:|DisjointClasses:|DisjointWith:)'

# expressão regular para identificar nomes de individuos
INDIVIDUALS_NAMES = r'\b[A-Z][a-zA-Z]*\d+\b'

# expressão regular para identificar caracteres especiais
SPECIAL_CARACTERES = r'[\(\)\[\]\{\}\,\<\>\"\=]'

# expressão regular para identificar classes
CLASS_IDENTIFIER = r'\b[A-Z][a-zA-Z]*(\s[A-Z][a-zA-Z]*)*\b(?!:)'

# expressão regular para identificar propriedades
PROPERTY_IDENTIFIER = r'\b([a-z][a-zA-Z]*|is[A-Z][a-zA-Z]*Of|has[A-Z][a-zA-Z])\b(?!:)'

# expressão regular para identificar tipos de dados
DATA_TYPE = r'\b(owl:|rfg:|rdfs:|xsd:|rational|real|langString|PlainLiteral|XMLLiteral|Literal|anyURI|base64Binary|boolean|byte|dateTime|dateTimeStamp|decimal|double|float|hexBinary|int|integer|language|long|Name|NCName|negativeInteger|NMTOKEN|nonNegativeInteger|string)\b'

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

#funções para identificar os tokens. cada função tem uma expressão regular que identifica o token(o que está dentro do parênteses de @token é a expressão regular que identifica aquele token) e retorna o token identificado.

#funçaõ para reconhecer números
def t_NUMBER(t):
    r'\b(\d+)\b'
    t.value = int(t.value)
    t.lexer.num_numbers += 1
    return t

#função para reconhecer palavras reservadas gerais(que podem ter variações de maiusculas e minusculas)
@TOKEN(RESERVED_GERAL)
def t_RESERVED_GERAL(t):
    t.type = reserved[t.value.lower()]
    t.lexer.num_reserved += 1
    return t
#função para reconhecer palavras reservadas que não tem variações de maiusculas e minusculas
@TOKEN(RESERVED_OTHERS)
def t_RESERVED_OTHERS(t):
    t.type = reserved[t.value.lower()]
    t.lexer.num_reserved += 1
    return t

#função para reconhecer tipos de dados.Se encontrar as palavras do regex (owl, xsd, rdfs, rdf) irá editar o tipo para NAMESPACEID. Caso seja qualquer outra palavra do regex, irá editar o tipo para DATA_TYPE
@TOKEN(DATA_TYPE)
def t_DATA_TYPE(t):
    t.type = namespacesAndTypes[t.value.lower()]
    if t.value == 'owl:' or t.value == 'xsd:' or t.value == 'rdfs:' or t.value == 'rdf:':
        t.type = 'NAMESPACEID'
        t.lexer.num_namespace_ids += 1
    else:
        t.type = 'DATA_TYPE'
        t.lexer.num_data_types += 1
    return t

#função para reconhecer nome de propriedades. Se encontrar as palavras do regex começando com "has" ou começando com "is" e terminando com "Of", irá editar o tipo para um property identifier especifico, sendo respectivamente PROPERTY_IDENTIFIER_has ou PROPERTY_IDENTIFIER_is_Of. Caso seja qualquer outra palavra do regex, irá editar o tipo para PROPERTY_IDENTIFIER
@TOKEN(PROPERTY_IDENTIFIER)
def t_PROPERTY_IDENTIFIER(t):
    if t.value.startswith("has"):
        t.type = "PROPERTY_IDENTIFIER_has"
    elif t.value.startswith("is") and t.value.endswith("Of"):
        t.type = "PROPERTY_IDENTIFIER_is_Of"
    else:
        t.type = "PROPERTY_IDENTIFIER"
    t.lexer.num_property_identifiers += 1
    return t

#função para reconhecer identificadores de classes
@TOKEN(CLASS_IDENTIFIER)
def t_CLASS_IDENTIFIER(t):
    t.lexer.num_class_identifiers += 1
    return t

#função para reconhecer nomes de individuos
@TOKEN(INDIVIDUALS_NAMES)
def t_INDIVIDUAL_NAMES(t):
    t.lexer.num_individual_names += 1
    t.type = "IndividualNames"
    return t

#função para reconhecer caracteres especiais
@TOKEN(SPECIAL_CARACTERES)
def t_SPECIAL_CHARACTERS(t):
    t.type = "SpecialCharacters"
    t.lexer.num_special_characters += 1
    return t

# função para reconhecer quebras de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# regex para ignorar espaços e tabulações
t_ignore = ' \t'

# função para ignorar comentários
def t_COMMENT(t):
    r'\#.*'
    pass

#função de erro. Se um bloco de caracteres não se encaixar em nenhum dos tokens acima, a função de erro abaixo é chamada.
def t_error(t):

    illegal_sequence = t.value[0]
    i = 1
    
    # Continua capturando enquanto os caracteres não forem reconhecidos e não forem espaços
    while i < len(t.value) and not t.value[i].isspace() and not any(t.value[i:].startswith(p) for p in ['+', '-', '*', '/', '(', ')']):
        illegal_sequence += t.value[i]
        i += 1
    
    
    if(t.value[0].isdigit()):
        print("nenhum token reconhecido começa com um número. Erro na linha", t.lineno)
    
    else:
        print(f"Sequencia ilegal: '{illegal_sequence}' na linha {t.lineno}")
    
    t.lexer.skip(len(illegal_sequence))


# constroi  o lexer e inicializa as variáveis(cria atributos no lexer) de contagem
lexer = lex.lex()
lexer.num_reserved = 0
lexer.num_individual_names = 0
lexer.num_special_characters = 0
lexer.num_numbers = 0
lexer.num_namespace_ids = 0
lexer.num_data_types = 0
lexer.num_property_identifiers = 0
lexer.num_class_identifiers = 0

# lendo o arquivo de entrada
file_path = 'input.txt'
with open(file_path, 'r') as file:
    data = file.read()

lexer.input(data)
#inicializa a tabela de símbolos(como é uma estrutura de dados do tipo set, não permite repetições)
simbol_table = set()
listaToken = []

# Dicionário para armazenar os tokens identificados
identified_tokens = {
    "Reserved Words": set(),
    "Namespaces": set(),
    "Individual Names": set(),
    "Special Characters": set(),
    "Property Identifiers": set(),
    "Class Identifiers": set(),
    "Data Types": set(),
    "Numbers": set(),
}

#para cada token, adiciona o token ao seu rescpetivo conjunto no dicionário de tokens identificados e adiciona o tipo do token à tabela de símbolos
while True:
    tok = lexer.token()
    if not tok:
        break
    simbol_table.add(tok.type)
    listaToken.append(tok)
    if tok.type in reserved.values():
        identified_tokens["Reserved Words"].add(tok.value)
    elif tok.type == "NAMESPACEID":
        identified_tokens["Namespaces"].add(tok.value)
    elif tok.type == "IndividualNames":
        identified_tokens["Individual Names"].add(tok.value)
    elif tok.type == "SpecialCharacters":
        identified_tokens["Special Characters"].add(tok.value)
    elif tok.type.startswith("PROPERTY_IDENTIFIER"):
        identified_tokens["Property Identifiers"].add(tok.value)
    elif tok.type == "CLASS_IDENTIFIER":
        identified_tokens["Class Identifiers"].add(tok.value)
    elif tok.type == "DATA_TYPE":
        identified_tokens["Data Types"].add(tok.value)
    elif tok.type == "NUMBER":
        identified_tokens["Numbers"].add(tok.value)

#imprime a quantidade de tokens identificados de cada tipo
print("=== Sumário ===")
print(f"Número de palavras reservadas: {lexer.num_reserved}")
print(f"Número de Nomes Individuais: {lexer.num_individual_names}")
print(f"Número de Caracteres Especiais: {lexer.num_special_characters}")
print(f"Número de Números: {lexer.num_numbers}")
print(f"Número de IDs de Namespace: {lexer.num_namespace_ids}")
print(f"Número de Tipos de Dados: {lexer.num_data_types}")
print(f"Número de Identificadores de Propriedades: {lexer.num_property_identifiers}")
print(f"Número de Identificadores de Classes: {lexer.num_class_identifiers}")

#imprime cada token único identificado de cada tipo
print("\n=== Tokens Detalhados ===")
for category, items in identified_tokens.items():
    print(f"\n{category}:")
    for item in sorted(items):
        print(f"  - {item}")



print('\n deseja ver todos os tokens encontrados em ordem no arquivo? \n formato de exibição: (TOKEN,valor,linha,posição na linha). s/n')

# imprime todos os tokens encontrados no arquivo no formato (TOKEN, valor, linha, posição na linha)
if(input().lower() == 's'):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
else :
    print('fim do programa')