# Escreva um programa para ler o peso de uma pessoa na Terra e o número de um planeta. Em seguida, o
# programa deve exibir o peso equivalente da pessoa no planeta escolhido.
# ID Planeta Gravidade
# 1 Mercúrio 0,37
# 2 Vênus 0,88
# 3 Marte 0,38
# 4 Júpiter 2,64
# 5 Saturno 1,15
# Para calcular o peso no planeta escolhido, usa-se a fórmula:
# PesoplanetaEscolhido = pesoTerra / 10.0 * gravidadeplanetaEscolhido
# Entrada
# Um número inteiro correspondendo ao ID do planeta que se deseja calcular o peso e um número
# fracionário correspondendo ao peso da pessoa na terra.
# Saída
# Um número fracionário com duas casas decimais correspondendo ao peso da pessoa no planeta
# escolhido.
# Exemplo de entrada Exemplo de saída
# 1 50 1.85
# 2 63 5.54
# 3 54 2.05
# 4 48 12.67
# 5 65

def calcular_peso_planeta(peso_terra, id_planeta):
    gravidades = {
        1: 0.37,
        2: 0.88,
        3: 0.38,
        4: 2.64,
        5: 1.15
    }
    
    if id_planeta in gravidades:
        gravidade = gravidades[id_planeta]
        peso_planeta = peso_terra / 10.0 * gravidade
        return f"{peso_planeta:.2f}"
    else:
        return "ID do planeta inválido."

# Exemplo de uso
id_planeta = int(input("Digite o ID do planeta: "))
peso_terra = float(input("Digite o peso na Terra: "))

print(calcular_peso_planeta(peso_terra, id_planeta))
