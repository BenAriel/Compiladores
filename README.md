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

5. **Tratamento de Erros**:
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




