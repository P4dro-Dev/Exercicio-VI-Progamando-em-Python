# Faça um programa para ler dois inteiros X e Y representando um ponto em um plano cartesiano.
# Imprima qual quadrante esse ponto se encontra. Caso o ponto não esteja em algum eixo, imprima apenas
# a mensagem "eixos".
# Entrada
# A entrada consiste de dois números inteiros: X e Y.
# Saída
# A saída consiste de uma linha contendo a mensagem indicando qual o quadrante que o ponto está.
# Exemplo de entrada Exemplo de saída
# 1
# 2
# Q1
# -2
# 2
# Q2
# -5
# -6
# Q3
# 4
# -1
# Q4
# 7
# 0
# eixos

def determinar_quadrante(X, Y):
    if X > 0 and Y > 0:
        return "Q1"
    elif X < 0 and Y > 0:
        return "Q2"
    elif X < 0 and Y < 0:
        return "Q3"
    elif X > 0 and Y < 0:
        return "Q4"
    else:
        return "eixos"

X = int(input("Digite o valor de X: "))
Y = int(input("Digite o valor de Y: "))

print(determinar_quadrante(X, Y))
