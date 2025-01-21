# Elabore um algoritmo que simule uma calculadora com as operações de soma, subtração, divisão e
# multiplicação. Para isso, o usuário informará um número inteiro, a operação que deseja realizar e outro
# número inteiro. O algoritmo deve reconhecer a operação informada pelo usuário e mostrar o valor do
# cálculo.
# Entrada
# Um número inteiro, um caractere representando a operação que o usuário deseja realizar (1 para soma, 2
# para subtração, 3 para multiplicação ou 4 para divisão) e outro número inteiro. Caso o usuário informe
# uma operação inválida, escreva “Operação inválida”.
# Saída
# A operação realizada e o valor resultante, conforme tabela abaixo:
# Exemplo de entrada Exemplo de saída
# 1 1 2 1 + 2 = 3.00
# 2 3 3 2 * 3 = 6.00
# 5 2 2 5 - 2 = 3.00
# 5 4 2 5 / 2 = 2.50
# 5 5 2 Operação inválida.

def calculadora(num1, operacao, num2):
    if operacao == 1:
        resultado = num1 + num2
        operacao_str = "+"
    elif operacao == 2:
        resultado = num1 - num2
        operacao_str = "-"
    elif operacao == 3:
        resultado = num1 * num2
        operacao_str = "*"
    elif operacao == 4:
        if num2 != 0:
            resultado = num1 / num2
            operacao_str = "/"
        else:
            return "Divisão por zero não é permitida."
    else:
        return "Operação inválida."

    return f"{num1} {operacao_str} {num2} = {resultado:.2f}"

num1 = int(input("Digite o primeiro número: "))
operacao = int(input("Digite a operação (1 para soma, 2 para subtração, 3 para multiplicação, 4 para divisão): "))
num2 = int(input("Digite o segundo número: "))

print(calculadora(num1, operacao, num2))
