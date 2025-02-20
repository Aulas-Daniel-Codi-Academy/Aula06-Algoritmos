# 1 - Introdução aos Algoritmos
# Conceito de Algoritmos e Ambiente de Programação
# Um algoritmo é uma sequência de passos bem definidos para resolver um problema.
# Eles podem ser representados de diversas formas, como fluxogramas, pseudocódigo ou código-fonte em linguagens de programação.
# O ambiente de programação refere-se ao conjunto de ferramentas utilizadas para desenvolver algoritmos,
# incluindo editores de código, compiladores ou interpretadores e depuradores.
# Python é uma linguagem interpretada, ou seja, seu código é executado linha por linha, sem necessidade de compilação prévia.

print("Olá, Mundo! Este é um exemplo básico de um programa em Python.")
print("Executando um segundo exemplo de introdução ao Python.")

# 2 - Noções de uma Linguagem de Programação
# Variáveis, Tipos de Dados e Operações Básicas
numero = 10
texto = "Exemplo de string"
booleano = True
print(f"Número: {numero}, Texto: {texto}, Booleano: {booleano}")

numero2 = 25
texto2 = "Outro exemplo de string"
booleano2 = False
print(f"Número: {numero2}, Texto: {texto2}, Booleano: {booleano2}")

# 3 - Procedimentos e Funções


def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo ao curso de Algoritmos."


print(saudacao("Daniel"))
print(saudacao("Thielmann"))

# 4 - Estruturas Condicionais
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

idade2 = 16
if idade2 >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# 5 - Estruturas de Repetição
for i in range(1, 10, 2):  # Começa do 1, vai até 10, pulando de 2 em 2
    print(f"Contagem: {i}")

for i in range(6):
    print(f"Contagem: {i}")

j = 0
while j < 5:
    print(f"Contagem com while: {j}")
    j += 1

# 6 - Vetores Numéricos
numeros = [10, 20, 30, 40, 50]
for num in numeros:
    print(num)

mais_numeros = [5, 15, 25, 35, 45]
for num in mais_numeros:
    print(num)

# 7 - Strings e Manipulação
frase = "Aprendendo Python"
print(frase.upper())
print(frase.split(" "))

outra_frase = "Programação é divertida"
print(outra_frase.lower())
print(outra_frase.replace("divertida", "interessante"))

# 8 - Matrizes (Listas Aninhadas)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz[1][2])  # Acessando elemento da matriz

outra_matriz = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
]
print(outra_matriz[2][0])  # Acessando outro elemento da matriz

# 9 - Estruturas Heterogêneas (Dicionários)
aluno = {
    "nome": "Daniel",
    "idade": 22,
    "curso": "Ciência da Computação"
}
print(f"Aluno: {aluno['nome']}, Curso: {aluno['curso']}")

outro_aluno = {
    "nome": "Thielmann",
    "idade": 24,
    "curso": "Engenharia de Software"
}
print(f"Aluno: {outro_aluno['nome']}, Curso: {outro_aluno['curso']}")
