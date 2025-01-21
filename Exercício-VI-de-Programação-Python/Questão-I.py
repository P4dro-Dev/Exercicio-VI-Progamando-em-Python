# A turma do primeiro semestre do Curso Técnico em Informática fará uma votação para escolher o líder
# da sala. Para auxiliar na apuração da votação, faça um algoritmo que receba o nome dos dois estudantes
# candidatos a líder e a quantidade de votos que cada um recebeu. Após isso, seu algoritmo deverá exibir o
# nome do estudante vencedor ou se houve Empate.
# Entrada
# O nome dos dois estudantes candidatos a líder e a quantidade de votos que cada um recebeu.
# Saída
# O nome do estudante vencedor. Exiba a mensagem “Empate”, caso não haja ganhador.
# Exemplo de entrada Exemplo de saída
# Joao
# Maria
# 10
# 10
# Empate
# Joao
# Maria
# 15
# 20
# Maria
# João
# Maria
# 20
# 15
# João

def apurar_votos(nome1, votos1, nome2, votos2):
    if votos1 > votos2:
        return nome1
    elif votos2 > votos1:
        return nome2
    else:
        return "Empate"

nome1 = input("Nome do primeiro candidato: ")
votos1 = int(input("Quantidade de votos do primeiro candidato: "))
nome2 = input("Nome do segundo candidato: ")
votos2 = int(input("Quantidade de votos do segundo candidato: "))

resultado = apurar_votos(nome1, votos1, nome2, votos2)
print(resultado)
