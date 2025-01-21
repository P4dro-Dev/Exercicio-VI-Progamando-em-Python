# Carnaval é um feriado normalmente comemorado em fevereiro. Em muitas cidades brasileiras, a
# principal atração são os desfiles das escolas de samba. As várias associações vão ao som dos seus
# sambas-enredos e são julgadas pela liga das escolas de samba para determinar o campeão do Carnaval.
# Cada grupo é avaliado em vários aspectos. Em cada aspecto, cada escola recebe cinco notas, variando de
# 5 a 10. A nota final da escola em um determinado aspecto é a soma das três notas do meio recebidas pela
# escola, excluindo a maior e a menor das cinco notas.
# O presidente da liga pediu que você escrevesse um programa que, dadas as notas da escola de samba,
# calcule sua nota final em um determinado aspecto.
# Entrada
# Cinco valores inteiros correspondendo as notas das escolas.
# Saída
# Um número correspondendo a nota da escola.
# Exemplo de entrada Exemplo de saída
# 10 9 9 9 8 27
# 10 10 10 10 10 30
# 10 9 8 7 6 24
# 10 9 9 8 8 26

def calcular_nota_final(notas):
    notas.sort()
    return sum(notas[1:4])

notas = [int(input("Nota: ")) for _ in range(5)]
nota_final = calcular_nota_final(notas)
print(f"Nota final: {nota_final}")
