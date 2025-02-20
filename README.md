# 📘 Guia Completo de Algoritmos

## 📌 Introdução

### O que é um Algoritmo?

Um **algoritmo** é uma sequência finita de passos bem definidos para resolver um problema. Ele pode ser representado em diferentes formas, como:

- **Pseudocódigo** (descrição textual próxima a uma linguagem de programação)
- **Fluxogramas** (representação gráfica com símbolos)
- **Código-fonte** (escrito em uma linguagem de programação, como Python ou JavaScript)

Os algoritmos são a base da computação, usados para resolver problemas, automatizar tarefas e desenvolver sistemas inteligentes.

---

## 🖥️ Ambiente de Programação

O ambiente de programação é o conjunto de ferramentas utilizadas para escrever, testar e executar algoritmos. Alguns componentes incluem:

- **Editor de Código**: VS Code, PyCharm, Sublime Text
- **Interpretadores & Compiladores**: Python, GCC, Node.js
- **Depuradores**: Ferramentas para encontrar erros no código
- **Ambientes Online**: Replit, Google Colab

Exemplo básico de código em Python:

```python
print("Olá, Mundo! Este é um exemplo básico de um programa em Python.")
```

---

## 🔢 Tipos de Dados e Variáveis

As variáveis armazenam valores que podem ser usados e manipulados pelo algoritmo. Os principais tipos de dados são:

| Tipo     | Descrição           | Exemplo                  |
| -------- | ------------------- | ------------------------ |
| Inteiro  | Números inteiros    | `10, -5, 1000`           |
| Float    | Números decimais    | `3.14, -0.99, 2.0`       |
| String   | Texto entre aspas   | `"Python" , 'Algoritmo'` |
| Booleano | Verdadeiro ou Falso | `True, False`            |

Exemplo de variáveis:

```python
numero = 10
texto = "Exemplo de string"
booleano = True
print(f"Número: {numero}, Texto: {texto}, Booleano: {booleano}")
```

---

## 🔄 Estruturas Condicionais

As estruturas condicionais permitem que o algoritmo tome decisões baseadas em condições.

Exemplo:

```python
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

---

## 🔁 Estruturas de Repetição

As repetições permitem executar um bloco de código várias vezes. Os principais tipos são:

### ✅ `for` - Loop controlado:

```python
for i in range(1, 6):  # Contagem de 1 a 5
    print(f"Contagem: {i}")
```

### 🔄 `while` - Loop baseado em condição:

```python
contador = 1
while contador <= 5:
    print(f"Contagem com while: {contador}")
    contador += 1
```

---

## 📚 Estruturas de Dados

### 📌 Listas (Vetores)

São sequências de elementos indexados.

```python
numeros = [10, 20, 30, 40, 50]
print(numeros[2])  # Saída: 30
```

### 🔢 Matrizes (Listas Aninhadas)

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz[1][2])  # Saída: 6
```

### 🗂️ Dicionários (Estruturas Heterogêneas)

```python
aluno = {"nome": "Daniel", "idade": 22, "curso": "Ciência da Computação"}
print(aluno["nome"])  # Saída: Daniel
```

---

## 🛠️ Funções e Procedimentos

As funções permitem reutilizar código e organizá-lo melhor.

```python
def saudacao(nome):
    return f"Olá, {nome}!"
print(saudacao("Daniel"))
```

---

## 🚀 Conclusão

Os algoritmos são essenciais para resolver problemas de forma eficiente. Compreender estruturas de controle, manipulação de dados e boas práticas facilita a criação de soluções escaláveis e otimizadas.

Quer aprender mais? Pratique escrevendo seus próprios algoritmos e explore problemas de lógica! 🚀
