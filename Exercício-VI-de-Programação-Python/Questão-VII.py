# Leia o código de um determinado produto e mostre sua classificação. Utilize a seguinte tabela como
# referência:
# Código Classificação
# 1 Alimento não-perecível
# 2, 3 ou 4 Alimento perecível
# 5 ou 6 Vestuário
# 7 Higiene pessoal
# 8, 9 ou 10 Limpeza e utensílios domésticos
# Qualquer outro código Código invalido
# Entrada
# Um número inteiro correspondendo ao código de um produto.
# Saída
# A classificação do produto, conforme a tabela apresentada anteriormente.
# Exemplo de entrada Exemplo de saída
# 1 Alimento não-perecível
# 2 Alimento perecível
# 5 Vestuário
# 7 Higiene pessoal
# 9 Limpeza e utensílios domésticos
# 11 Código invalido

def classificar_produto(codigo):
    if codigo == 1:
        return "Alimento não-perecível"
    elif codigo in [2, 3, 4]:
        return "Alimento perecível"
    elif codigo in [5, 6]:
        return "Vestuário"
    elif codigo == 7:
        return "Higiene pessoal"
    elif codigo in [8, 9, 10]:
        return "Limpeza e utensílios domésticos"
    else:
        return "Código invalido"

codigo = int(input("Digite o código do produto: "))
print(classificar_produto(codigo))
