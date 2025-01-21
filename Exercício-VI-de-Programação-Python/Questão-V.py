# Reajuste Salarial
# Programa para calcular o reajuste salarial de um funcionário
# Lê o salário do funcionário
salario = float(input("Digite o salário do funcionário: "))

# Verifica a faixa salarial e calcula o reajuste
if salario <= 2000:
    reajuste = salario * 0.15
else:
    reajuste = salario * 0.10

# Calcula o novo salário após o reajuste
novo_salario = salario + reajuste

# Exibe o novo salário
print(f"O novo salário é: R$ {novo_salario:.2f}")

# Equilíbrio do Móbile:

# Programa para verificar o equilíbrio do móbile
# Lê os pesos das bolas A, B, C e D
A, B, C, D = map(int, input("Digite os pesos das bolas A, B, C e D: ").split())

# Verifica se as condições de equilíbrio são satisfeitas
if A == B + C + D and B + C == D and B == C:
    print("S")  # Móbile está equilibrado
else:
    print("N")  # Móbile não está equilibrado
