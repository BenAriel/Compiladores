from Lex import lexer, init_lexer
from Sintatico import parser

# Inicializa o lexer com contadores zerados
init_lexer(lexer)

if __name__ == "__main__":
    try:
        # Define o nome do arquivo de entrada
        input_file = "input.txt"

        # Lê o conteúdo do arquivo
        with open(input_file, "r", encoding="utf-8") as file:
            data = file.read()

        # Reinicia o lexer e fornece os dados a ele
        lexer.input(data)

        # Exibe cada token identificado pelo lexer
        print("Tokens reconhecidos no arquivo:")
        while True:
            token = lexer.token()
            if not token:
                break
            print(f"Token reconhecido: {token.type} (Valor: '{token.value}', Linha: {token.lineno})")

        # Faz o parsing do conteúdo do arquivo
        print("\nIniciando parsing do arquivo...")
        lexer.lineno = 1
        result = parser.parse(data, lexer=lexer)

        # Exibe a árvore sintática resultante
        print("\nÁrvore Sintática:", result)

    except FileNotFoundError:
        print(f"Erro: Arquivo '{input_file}' não encontrado.")
    except Exception as e:
        print("Ocorreu um erro:", str(e))
