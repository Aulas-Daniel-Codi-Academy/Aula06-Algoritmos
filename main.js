// 1 - Introdução aos Algoritmos
// Conceito de Algoritmos e Ambiente de Programação
console.log(
  "Olá, Mundo! Este é um exemplo básico de um programa em JavaScript."
);
console.log("Executando um segundo exemplo de introdução ao JavaScript.");

// 2 - Noções de uma Linguagem de Programação
// Variáveis, Tipos de Dados e Operações Básicas
let numero = 10;
let texto = "Exemplo de string";
let booleano = true;
console.log(`Número: ${numero}, Texto: ${texto}, Booleano: ${booleano}`);

let numero2 = 25;
let texto2 = "Outro exemplo de string";
let booleano2 = false;
console.log(`Número: ${numero2}, Texto: ${texto2}, Booleano: ${booleano2}`);

// 3 - Procedimentos e Funções
function saudacao(nome) {
  return `Olá, ${nome}! Bem-vindo ao curso de Algoritmos.`;
}
console.log(saudacao("Daniel"));
console.log(saudacao("Thielmann"));

// 4 - Estruturas Condicionais
let idade = 18;
if (idade >= 18) {
  console.log("Você é maior de idade.");
} else {
  console.log("Você é menor de idade.");
}

let idade2 = 16;
if (idade2 >= 18) {
  console.log("Você é maior de idade.");
} else {
  console.log("Você é menor de idade.");
}

// 5 - Estruturas de Repetição
for (let i = 1; i < 5; i++) {
  console.log(`Contagem: ${i}`);
}

for (let i = 0; i < 6; i++) {
  console.log(`Contagem: ${i}`);
}

let j = 0;
while (j < 5) {
  console.log(`Contagem com while: ${j}`);
  j++;
}

// 6 - Vetores Numéricos
let numeros = [10, 20, 30, 40, 50];
numeros.forEach((num) => console.log(num));

let maisNumeros = [5, 15, 25, 35, 45];
maisNumeros.forEach((num) => console.log(num));

// 7 - Strings e Manipulação
let frase = "Aprendendo JavaScript";
console.log(frase.toUpperCase());
console.log(frase.split(" "));

let outraFrase = "Programação é divertida";
console.log(outraFrase.toLowerCase());
console.log(outraFrase.replace("divertida", "interessante"));

// 8 - Matrizes (Arrays Multidimensionais)
let matriz = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];
console.log(matriz[1][2]); // Acessando elemento da matriz

let outraMatriz = [
  [10, 11, 12],
  [13, 14, 15],
  [16, 17, 18],
];
console.log(outraMatriz[2][0]); // Acessando outro elemento da matriz

// 9 - Estruturas Heterogêneas (Objetos)
let aluno = {
  nome: "Daniel",
  idade: 22,
  curso: "Ciência da Computação",
};
console.log(`Aluno: ${aluno.nome}, Curso: ${aluno.curso}`);

let outroAluno = {
  nome: "Thielmann",
  idade: 24,
  curso: "Engenharia de Software",
};
console.log(`Aluno: ${outroAluno.nome}, Curso: ${outroAluno.curso}`);
