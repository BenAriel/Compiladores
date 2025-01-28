import ply.yacc as yacc
from Lex import tokens  # Importa os tokens definidos no léxico

# Conjunto inicial de regras de produção
global x
x = True
vetorAntes = []
vetorDepois = []

def p_statements(p):
    '''statements : Class CLASS_IDENTIFIER statement_defined_class statements
                  | Class CLASS_IDENTIFIER statement_defined_class
                  | Class CLASS_IDENTIFIER statement_primitive_class
                  | Class CLASS_IDENTIFIER statement_primitive_class statements
                  | empty'''
    global x
    x = True
    pass

def p_statement_defined_class(p):
    '''statement_defined_class : EquivalentTo_possible maybe_suclassof statement_class_disjoin statement_class_individuals '''  
    
def p_statement_primitive_class(p):
    '''statement_primitive_class : subclassof_possible statement_class_disjoin statement_class_individuals'''

def p_EquivalentTo_possible(p):
    '''EquivalentTo_possible : EquivalentTo nested
                             | EquivalentTo statement_closed_axiom_class
                             | EquivalentTo statement_enumerated_class
                             | EquivalentTo statement_covered_class
                             | EquivalentTo JustDefined
                             '''
    global vetorAntes
    vetorAntes.clear()
    pass

def p_maybe_suclassof(p):
    '''maybe_suclassof : subclassof_possible
                       | empty'''
    pass

def p_subclassof_possible(p):
    '''subclassof_possible : SubClassOf nested
                           | SubClassOf statement_closed_axiom_class
                           | SubClassOf statement_enumerated_class
                           | SubClassOf statement_covered_class
                           | SubClassOf primitive_class_mandatory'''
    global vetorAntes
    vetorAntes.clear()
    pass

def p_justDefined(p):
    '''JustDefined : CLASS_IDENTIFIER COMMA expression statement_class_disjoin statement_class_individuals
    | CLASS_IDENTIFIER AND expression statement_class_disjoin statement_class_individuals
    | expression statement_class_disjoin statement_class_individuals
    | CLASS_IDENTIFIER
    | empty'''
    global x
    if (x == True):
        print(f"Classe definida normal: {p[-2]}")
        print("")
    else:
        print("erro na classe definida " + p[-2] + ". erro de sobrecarregamento ou corsão." ) 
        print("")
    pass


def p_operators(p):
    '''operators : MIN
                 | MAX
                 | EXACTLY '''
    p[0] = p[1]

def p_statement_reserved_word(p):
    '''statement_reserved_word : SOME
                               | OR
                               | AND
                               | VALUE'''
    p[0] = p[1]

def p_statement_others_reserved_word(p):
    '''statement_others_reserved_word : SOME
                               | MIN
                               | ONLY
                               | EXACTLY
                               | OR
                               | MAX
                               | AND'''
    p[0] = p[1]

def p_statement_property_identify(p):
    '''statement_property_identify : PROPERTY_IDENTIFIER_has
                                   | PROPERTY_IDENTIFIER_is_Of
                                   | PROPERTY_IDENTIFIER'''
    p[0] = p[1]

def p_primitive_class_mandatory(p):
    '''primitive_class_mandatory : CLASS_IDENTIFIER COMMA expression statement_class_disjoin statement_class_individuals
                                 | CLASS_IDENTIFIER AND expression statement_class_disjoin statement_class_individuals
                                 | expression statement_class_disjoin statement_class_individuals
                                 | CLASS_IDENTIFIER
                                 | empty  '''
    global x
    if (x == True):
        print(f"Classe primitiva normal: {p[-2]}")
        print("")
    else:
        print("erro na classe primitiva" + p[-2] + ". erro de sobrecarregamento ou corsão." ) 
        print("")
    pass

def p_statement_class_disjoin(p):
    '''statement_class_disjoin : empty
                               | DisjointClasses statement_class_disjoin_check
                               | DisjointWith statement_class_disjoin_check'''
    pass

def p_statement_class_disjoin_check(p):
    '''statement_class_disjoin_check : CLASS_IDENTIFIER
                                     | CLASS_IDENTIFIER COMMA statement_class_disjoin_check'''
    pass

def p_statement_class_individuals(p):
    '''statement_class_individuals : empty
                                   | Individuals statement_class_individuals_check'''
    pass

def p_statement_class_individuals_check(p):
    '''statement_class_individuals_check : IndividualNames
                                         | IndividualNames COMMA statement_class_individuals_check'''
    pass

def p_statement_defined_class_equivalent(p):
    '''statement_defined_class_equivalent : statement_property_identify statement_reserved_word CLASS_IDENTIFIER RIGHT_PAREN
    | statement_property_identify statement_reserved_word CLASS_IDENTIFIER RIGHT_PAREN COMMA statement_defined_class_equivalent
                                          | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET RIGHT_PAREN
                                          | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET RIGHT_PAREN COMMA statement_defined_class_equivalent '''
    pass

def p_statement_operator_symbol(p):
    '''statement_operator_symbol : LESS_THAN
    | GREATER_THAN
    | EQUALS
    | GREATER_THAN EQUALS
    | LESS_THAN EQUALS'''

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]


def p_usually_inside_paren(p):
    '''usually_inside_paren : statement_property_identify statement_reserved_word CLASS_IDENTIFIER
    | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE
    | statement_property_identify operators NUMBER NAMESPACEID DATA_TYPE
    | statement_property_identify operators NUMBER CLASS_IDENTIFIER
    | statement_property_identify statement_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET
    | statement_property_identify'''
    
    global vetorAntes

    
    if (len(p) == 4):
        vetorAntes.append(p[3])
    elif (len(p) == 5):
        vetorAntes.append(p[4])
    
    if len(p) == 4 and isinstance(p[2],str) and isinstance(p[3],str):
        print("Propriedade : ", p[1] + " tipo: object property")
    elif len(p) == 5 and isinstance(p[2],str) and isinstance(p[3],str) and isinstance(p[4],str):
        print("propriedade : ", p[1] + " tipo: data property")
    elif len(p) == 6 and isinstance(p[2],str) and isinstance(p[3],int) and isinstance(p[4],str) and isinstance(p[5],str):
        print("propriedade : ", p[1] + " tipo: data property")
    elif len(p) == 5 and isinstance(p[2],str) and isinstance(p[3],int) and isinstance(p[4],str):
        print("propriedade : ", p[1] + " tipo: object property")
    elif len(p) == 9 and isinstance(p[2],str) and isinstance(p[3],str) and isinstance(p[4],str) and isinstance(p[5],str) and (isinstance(p[6],str) or callable(p[6])) and isinstance(p[7],int)  and isinstance(p[8],str):
        if p[4] == "integer":
            print("propriedade : ", p[1] + " tipo: data property")
        else:
            x = False
            print("Tipo de dado inválido. deve ser integer ou float")
    elif len(p) == 2:
        pass
    else:
        x = False
        print("Erro na definição da propriedade")


def p_usually_others_inside_paren(p):
    '''usually_others_paren : statement_property_identify statement_others_reserved_word CLASS_IDENTIFIER
    | statement_property_identify statement_others_reserved_word LEFT_PAREN usually_others_others_paren
    | statement_property_identify statement_others_reserved_word NAMESPACEID DATA_TYPE
    | statement_property_identify statement_others_reserved_word NUMBER NAMESPACEID DATA_TYPE
    | statement_property_identify statement_others_reserved_word NUMBER CLASS_IDENTIFIER
    | statement_property_identify statement_others_reserved_word NAMESPACEID DATA_TYPE LEFT_BRACKET statement_operator_symbol NUMBER RIGHT_BRACKET
    '''

def p_usually_others_others_inside_paren(p):
    ''' usually_others_others_paren : CLASS_IDENTIFIER RIGHT_PAREN
                                    | CLASS_IDENTIFIER OR usually_others_others_paren'''

def p_simple_paren(p):
    '''simple_paren : LEFT_PAREN usually_inside_paren RIGHT_PAREN'''
    pass

def p_simple_other_paren(p):
    '''simple_other_paren : LEFT_PAREN usually_others_paren RIGHT_PAREN'''
    pass

def p_expression_only(p):
    '''expression_only : CLASS_IDENTIFIER OR expression_only 
                        | CLASS_IDENTIFIER''' 
pass

def p_expression(p):
    '''expression : usually_inside_paren
                            | usually_inside_paren COMMA expression
                            | simple_paren
                            | simple_paren COMMA expression
                            | simple_paren AND expression'''
    
def p_other_expression(p):
    '''other_expression : usually_inside_paren
                            | usually_others_paren
                            | usually_inside_paren COMMA other_expression
                            | usually_others_paren COMMA other_expression
                            | simple_other_paren
                            | simple_other_paren COMMA other_expression
                            | simple_other_paren AND other_expression
                            | usually_others_paren AND other_expression
                            | usually_inside_paren AND other_expression
                            '''

# Classes aninhadas
def p_statement_aninhada_class(p):
    '''nested : CLASS_IDENTIFIER AND nested_descriptions
                |  CLASS_IDENTIFIER COMMA nested_descriptions'''
    
    if (p[-1] == "SubClassOf:"):
        print(f"Classe primaria Primitiva, Classe secundaria aninhada: {p[-2]}")
        print("")
    else:
        print(f"Classe primaria Definida, Classe secundaria aninhada: {p[-2]}")
        print("")

def p_nested_descriptions(p):
    '''nested_descriptions : nested_descriptions AND nested_descriptions
                           | nested_descriptions OR nested_descriptions
                           | LEFT_PAREN nested_descriptions RIGHT_PAREN
                           | statement_property_identify statement_others_reserved_word nested_descriptions
                           | statement_property_identify statement_others_reserved_word CLASS_IDENTIFIER
                           | statement_property_identify statement_others_reserved_word VALUE CLASS_IDENTIFIER
                           | statement_property_identify statement_others_reserved_word VALUE IndividualNames
                           | CLASS_IDENTIFIER statement_others_reserved_word nested_descriptions
                           | statement_property_identify VALUE IndividualNames
                           | statement_property_identify VALUE CLASS_IDENTIFIER
                           | statement_property_identify statement_others_reserved_word VALUE nested_descriptions
                           | statement_property_identify statement_others_reserved_word NUMBER nested_descriptions
                           | statement_property_identify statement_others_reserved_word ONLY CLASS_IDENTIFIER
                           | statement_property_identify statement_others_reserved_word ONLY nested_descriptions
                           | statement_property_identify statement_others_reserved_word SOME CLASS_IDENTIFIER
                           | statement_property_identify statement_others_reserved_word SOME nested_descriptions
                           | CLASS_IDENTIFIER'''
    if len(p) == 4:
        if p[2] in ["AND", "OR"]:
            p[0] = f"({p[1]} {p[2]} {p[3]})"
        else:
            p[0] = f"{p[1]} {p[2]} {p[3]}"
    elif len(p) == 3:
        p[0] = f"({p[2]})"
    else:
        p[0] = f"{p[1]}"

def p_axiom_function(p):
    '''axiom_function : CLASS_IDENTIFIER
                      | CLASS_IDENTIFIER OR axiom_function'''
    
    global vetorDepois
    if not p[1] in vetorDepois:
        vetorDepois.append(p[1])

# Classes com axiomas fechados
def p_statement_closed_axiom_class(p):
    '''statement_closed_axiom_class : CLASS_IDENTIFIER COMMA expression ONLY LEFT_PAREN axiom_function RIGHT_PAREN
                |  CLASS_IDENTIFIER AND expression ONLY LEFT_PAREN axiom_function RIGHT_PAREN
                |  CLASS_IDENTIFIER expression ONLY LEFT_PAREN axiom_function RIGHT_PAREN
                |  CLASS_IDENTIFIER COMMA expression ONLY axiom_function
                |  CLASS_IDENTIFIER AND expression ONLY axiom_function
                |  CLASS_IDENTIFIER expression ONLY axiom_function'''
    
    global vetorAntes
    
    for elemento in vetorAntes[:]:
        if elemento in vetorDepois:
            vetorDepois.remove(elemento)
            vetorAntes.remove(elemento)
    
    if (len(vetorDepois) == 0) and (len(vetorAntes) == 0):
        if (p[-1] == "SubClassOf:"):
            print(f"Classe primaria Primitiva, Classe secundaria fechamento: {p[-2]}")
            print("")
        else:
            print(f"Classe primaria Definida, Classe secundaria fechamento: {p[-2]}")
            print("")
    else:
        p_error_closed_axiom("o número de classificadores de identidade declarados não é igual ao número de classificadores de identidade usados no only")

def p_error_closed_axiom(p):
    print("Erro: ", p)
    
# Classes enumeradas
def p_statement_enumerated_class(p):
    '''statement_enumerated_class : LEFT_CURLY_BRACKET statement_enumerated_class_check RIGHT_CURLY_BRACKET'''
    
    if (p[-1] == "SubClassOf:"):
        print(f"Classe primaria Primitiva, Classe secundaria enumerado: {p[-2]}")
        print("")
    else:
        print(f"Classe primaria Definida, Classe secundaria enumerado: {p[-2]}")
        print("")

def p_statement_enumerated_class_check(p):
    '''statement_enumerated_class_check : IndividualNames
                                        | IndividualNames COMMA statement_enumerated_class_check'''
    pass

# Classes cobertas
def p_statement_covered_class(p):
    '''statement_covered_class : statement_covered_class_check'''
    
    if (p[-1] == "SubClassOf:"):
        print(f"Classe primaria Primitiva, Classe secundaria coberta: {p[-2]}")
        print("")
    else:
        print(f"Classe primaria Definida, Classe secundaria coberta: {p[-2]}")
        print("")

def p_statement_covered_class_check(p):
    '''statement_covered_class_check : CLASS_IDENTIFIER
                                     | CLASS_IDENTIFIER OR statement_covered_class_check'''
    pass

# Produção vazia
def p_empty(p):
    'empty :'
    pass

# Tratamento de erros
def p_error(p):
    if p:
        print(f"\nErro sintático detectado no token '{p.value}' (tipo: {p.type}) na linha {p.lineno}.")
        
        # Erros relacionados às Classes
        if p.type == "CLASS_IDENTIFIER":
            print(f"Erro no nome da classe '{p.value}'. Verifique se a classe está definida corretamente.")
            print("Certifique-se de que a classe segue o padrão de nomeação esperado para classes OWL, como: Customer, Pizza, Employee.")
        
        # Erros relacionados a palavras reservadas OWL
        elif p.type == "EQUIVALENTTO":
            print(f"Erro no uso de 'EquivalentTo' para a classe '{p.value}'. Verifique a expressão para garantir que ela seja composta de forma adequada.")
            print("O token 'EquivalentTo' é usado para definir uma equivalência de classe.")
        elif p.type == "SUBCLASSOF":
            print(f"Erro no uso de 'SubClassOf' para a classe '{p.value}'. Certifique-se de que a relação de subclasse está definida corretamente.")
            print("O token 'SubClassOf' é usado para indicar que uma classe é uma subclasse de outra.")
        elif p.type == "DISJOINTCLASSES":
            print(f"Erro no uso de 'DisjointClasses' para a classe '{p.value}'. Verifique a relação de classes disjuntas.")
            print("O token 'DisjointClasses' é usado para indicar que classes não compartilham membros em comum.")
        elif p.type == "SOME":
            print(f"Erro no uso de 'some' na definição de restrição para a classe '{p.value}'. Verifique se a restrição foi corretamente especificada.")
            print("O token 'some' é usado para indicar uma restrição existencial.")
        elif p.type == "ONLY":
            print(f"Erro no uso de 'only' na definição de restrição para a classe '{p.value}'. Verifique a restrição de valores permitidos.")
            print("O token 'only' é usado para indicar uma restrição universal.")

        # Erros relacionados a Individuos
        elif p.type == "INDIVIDUALNAME":
            print(f"Erro no nome do indivíduo '{p.value}'. Verifique se o nome do indivíduo está corretamente definido.")
            print("Os indivíduos devem ser nomes únicos, como: Customer1, Chef1, AmericanaHotPizza1.")
        
        # Erros com tipo de dado XSD
        elif p.type == "XSD_TYPE":
            print(f"Erro no tipo de dado '{p.value}'. Verifique se o tipo de dado foi utilizado corretamente.")
            print("Exemplos de tipos XSD válidos são: xsd:string, xsd:integer.")
        
        # Erros relacionados a valores ou expressões
        elif p.type == "NUMBER":
            print(f"Erro no número '{p.value}'. Verifique se a expressão numérica está no formato correto.")
            print("Exemplo de restrição numérica válida: [>= 400], [< 400].")
        
        # Erros gerais em parênteses ou vírgulas
        elif p.type in ["LEFT_PAREN", "RIGHT_PAREN", "COMMA"]:
            print(f"Erro no uso de parênteses ou vírgula: '{p.value}'.")
            print("Verifique o aninhamento correto de parênteses ou a separação adequada de tokens com vírgulas.")
        
        else:
            print(f"Erro no token OWL: '{p.value}'. Esse token pode não ser reconhecido ou estar fora de contexto.")
            print("Verifique se os tokens estão sendo usados corretamente em relação à sintaxe OWL.")
        
        print("Certifique-se de que as expressões OWL estão corretamente estruturadas, com classes, propriedades, axiomas e indivíduos definidos corretamente.")
        print("")

    else:
        print("\nErro sintático: fim inesperado da entrada. Pode faltar um token necessário como uma classe, propriedade ou axioma.")
        print("")


# Criar o parser
parser = yacc.yacc()