## **Sumário**

1. [Descrição do Projeto](#Analisador-Léxico-com-ply)  
2. [Objetivo](#objetivo)  
3. [Instalação e Configuração](#instalação-e-configuração)  
   3.1. [Pré-requisitos](#pré-requisitos) 
4. [Como Usar](#como-usar)  
5. [Funcionamento do Programa](#funcionamento-do-programa)  
   5.1. [Tokens Reconhecidos](#tokens-reconhecidos)  
   5.2. [Etapas Principais](#etapas-principais)  
6. [Exemplo de Saída](#exemplo-de-saída)
7. [Analisador Sintático com PLY](#analisador-sintático-com-ply)
8. [Analisador Semântico com PLY](#analisador-semântico-com-ply)


# Analisador Léxico com PLY

Este projeto implementa um analisador léxico para uma linguagem baseada em OWL2 (Web Ontology Language) utilizando a biblioteca [PLY](https://www.dabeaz.com/ply/), que fornece ferramentas para análise léxica e sintática em Python.


---

## **Objetivo**

O objetivo principal do programa é realizar a análise léxica de um arquivo de entrada, identificando tokens específicos relacionados a palavras reservadas, identificadores de propriedades, classes, namespaces, tipos de dados,cardinalidades(números) e caracteres especiais,além de guardar esses tokens em uma tabela de símbolos,para uso posterior na análise sintática. Além disso, ele gera um relatório detalhado do número e tipos de tokens encontrados no arquivo.

---

## **Instalação e Configuração**

### **Pré-requisitos**

1. **Python 3.8 ou superior**:
   - Baixe e instale o Python a partir do [site oficial](https://www.python.org/downloads/).

2. **Bibliotecas Necessárias**:
   - A biblioteca `ply` é requerida. Para instalá-la, utilize o comando abaixo no diretório em que o script python está:
     ```bash
     pip install ply
     ```

3. **Arquivo de Entrada**:
   - O programa processa um arquivo de texto chamado `input.txt`, que deve estar no mesmo diretório do script Python.

---

## **Como Usar**

1. **Preencha o arquivo `input.txt`**:
   - Insira o código ou texto a ser analisado dentro do arquivo `input.txt`. O arquivo por padrão vem com o teste enviado junto ao arquivo do trabalho.

2. **Execute o programa**:
   - No terminal, execute o script:
     ```bash
     python Lex.py
     ```

   - Ou utilize alguma IDE para rodar o programa.

3. **Interação no Terminal**:
   - O programa exibirá um resumo dos tokens encontrados.
   - Você será questionado se deseja visualizar todos os tokens detalhadamente. Responda com `s` (sim) ou `n` (não).

---

## **Funcionamento do Programa**

### **Tokens Reconhecidos**

O analisador identifica os seguintes tokens:
- **Operadores Aritméticos**: `+`, `-`, `*`, `/`.
- **Cardinalidades**: números.
- **Palavras Reservadas**: como `not`, `and`, `or`, `some`, `class:`, etc.
- **Identificadores**:
  - Propriedades (`hasX`, `isXOf`).
  - Classes (`ClassName`).
- **Nomes de Indivíduos**: Sequências que seguem um padrão específico.
- **Tipos de Dados**: Exemplo: `xsd:int`, `owl:Literal`.
- **Caracteres Especiais**: `()[]{},<>="`.

### **Etapas Principais**

1. **Definição de Tokens**:
   - Cada token é definido usando expressões regulares.
   - As expressões abrangem palavras reservadas, namespaces, tipos de dados e identificadores.

2. **Análise do Arquivo de Entrada**:
   - O arquivo `input.txt` é lido e processado pelo analisador léxico.
   - Os tokens são identificados, categorizados e contados.

3. **Resumo e Relatório**:
   - O programa exibe:
     - Quantidade de cada tipo de token.
     - Listas detalhadas dos tokens encontrados, organizados por categoria.

4. **Exibição Detalhada**:
   - Caso solicitado, o programa lista cada token encontrado no formato `(TOKEN, valor, linha, posição)`.

5. **Armazenamento na tabela de símbolos**:
   - Os tokens são armazenados em uma estrutura de dados do tipo Set(ou seja,não permite repetições) que servirá como tabela de símbolos na análise sintática.

6. **Tratamento de Erros**:
   - Sequências não reconhecidas são tratadas e exibidas com mensagens informativas.

---

## Exemplo de Saída

### Entrada (input.txt):  
  
Class: Customer  
  
 EquivalentTo:  
 Person  
 and (purchasedPizza some Pizza)  
 and (hasPhone some xsd:string)  

### Saída:  
=== Sumário ===  
• Número de palavras reservadas: 6  
• Número de Nomes Individuais: 0  
• Número de Caracteres Especiais: 4  
• Número de Números: 0  
• Número de IDs de Namespace: 1  
• Número de Tipos de Dados: 1  
• Número de Identificadores de Propriedades: 2  
• Número de Identificadores de Classes: 3  

=== Tokens Detalhados ===

Reserved Words:
  - Class:
  - EquivalentTo:
  - and
  - some

Namespaces:
  - xsd:

Individual Names:

Special Characters:
  - (
  - )

Property Identifiers:
  - hasPhone
  - purchasedPizza

Class Identifiers:
  - Customer
  - Person
  - Pizza

Data Types:
  - string

Numbers:

# Analisador Sintático com PLY
Este projeto implementa um analisador sintático para uma linguagem baseada em OWL2 (Web Ontology Language) utilizando a biblioteca [PLY](https://www.dabeaz.com/ply/), que fornece ferramentas para análise léxica e sintática em Python.


---

## **Objetivo**
O objetivo principal de um analisador sintático é verificar se uma sequência de tokens (gerados pelo analisador léxico) está estruturada de acordo com as regras gramaticais de uma linguagem formal. Em outras palavras, ele valida a sintaxe do código que é o nosso arquivo input.txt, assegurando que ele segue a gramática definida para a linguagem.

## **Como Usar**

1. **Preencha o arquivo `input.txt`**:
   - Insira o código ou texto a ser analisado dentro do arquivo `input.txt`. O arquivo por padrão vem com o teste enviado junto ao arquivo do trabalho.

2. **Execute o programa**:
   - No terminal, execute o script:
     ```bash
     python main.py
     ```

   - Ou utilize alguma IDE para rodar o programa.

3. **Interação no Terminal**:
   - O programa exibirá um resumo das classes sintáticas encontrados.

---

## **Funcionamento do Programa**

### **Etapas Principais**

1. **Definição das gramáticas**:
   - Cada gramática será única para seu tipo de classe.
   - Exceto as gramáticas auxiliares que combinam diferentes estruturas para formação da classe.
     
2. **Análise do Arquivo de Entrada**:
   - O arquivo `input.txt` é lido e processado pelo analisador léxico gerando os tokens.
   - Os tokens são identificados e o analisador sintático vai validando a estrutura a partir das regras gramaticais.

3. **Resumo e Relatório**:
   - O programa exibe:
     - As classes com sua classe primaria sendo Primitiva ou Definida e podendo ter ou não classe secundaria, podendo ser Coberta, Fechamento, Numerada, Aninhada.

4. **Tratamento de Erros**:
   - Sequências não reconhecidas são tratadas e exibidas com mensagens informativas.

---

## Exemplo de Saída

### Entrada (input.txt):  
  
Class: InterestingPizza

 EquivalentTo:
 
 Pizza
 
 and (hasTopping min 3 PizzaTopping)
 

 Class: SpicyPizza
 
 EquivalentTo:
 
 Pizza
 
 and (hasTopping some (hasSpiciness value Hot1)) 

### Saída:  
Iniciando parsing do arquivo...

Classe definida normal: InterestingPizza

Classe primaria Definida, Classe secundaria aninhada: SpicyPizza 

# Analisador Semântico com PLY
Este projeto implementa um analisador semântico para uma linguagem baseada em OWL2 (Web Ontology Language), estendendo o analisador sintático previamente construído. Ele utiliza a biblioteca PLY para análise léxica e sintática, além de implementar técnicas de análise semântica específicas.


---

## **Objetivo**
O objetivo principal do analisador semântico é validar semanticamente a estrutura da linguagem OWL, auxiliando o ontologista a:

- Garantir a ordem correta dos operadores de cabeçalho: As palavras-chave como Class, EquivalentTo, SubClassOf, DisjointClasses e Individuals devem seguir uma ordem específica.
- Validar tipos e intervalos de data properties: Assegura que os tipos e faixas de valores atribuídos às propriedades sejam corretamente definidos.
- Classificar propriedades: Diferencia entre data properties e object properties, com base nos termos que sucedem cada propriedade.

## **Como Usar**

1. **Preencha o arquivo `input.txt`**:
   - Insira o código ou texto a ser analisado dentro do arquivo `input.txt`. O arquivo por padrão vem com o teste enviado junto ao arquivo do trabalho.

2. **Execute o programa**:
   - No terminal, execute o script:
     ```bash
     python main.py
     ```

   - Ou utilize alguma IDE para rodar o programa.

3. **Interação no Terminal**:
   - O programa exibirá um resumo das classes sintáticas encontrados.

---

## **Funcionamento do Programa**

### **Etapas Principais**

1. **Análise da Precedência dos Operadores**:
   - alida a ordem dos cabeçalhos, como Class, EquivalentTo e SubClassOf.
   - Identifica ocorrências de cabeçalhos fora da ordem esperada e exibe mensagens de erro informativas.
     
2. **Verificação Estática de Tipos por Coerção**:
   - Confere a coerência dos tipos atribuídos a propriedades de dados (data properties).
   - Valida faixas de valores quando aplicável (e.g., xsd:integer[>=400]).

3. **Verificação Estática de Tipos por Sobrecarga:**:
   - Classifica propriedades como data properties ou object properties, analisando os termos que sucedem cada propriedade (e.g., hasPhone some xsd:string ou emitsReport some EvaluationReport).
    

4. **Tratamento de Erros**:
   - Mensagens claras exibidas para declarações semânticas inválidas, indicando o tipo de erro e sua localização.

---

## Exemplo de Saída

### Entrada (input.txt):  
  
 Class: Customer
 
 EquivalentTo:
 
 Person
 
 and (purchasedPizza some Pizza)

 and (hasPhone some xsd:string)
 
 Individuals:
 
 Customer1,
 
 Customer10,
 
 Customer2,
 
 Customer3,
 
 Customer4,
 
 Customer5,
 
 Customer6,
 
 Customer7,
 
 Customer8,
 
 Customer9
 

### Saída:  
Iniciando parsing do arquivo...

Propriedade : purchasedPizza

tipo: object property

propriedade :  hasPhone tipo: data property

Classe definida normal: 

Customer

