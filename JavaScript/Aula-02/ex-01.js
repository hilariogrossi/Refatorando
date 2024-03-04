/*Declarando Variável*/

/*var x = 20;
let y = 20;
const z = 30;*/

var globalVar_1 = '\nEu sou global!\n'; // Variável Global.

function testFunction_1() {
    console.log(globalVar_1);

}

testFunction_1();



function testFunction_2() {
    var globalVar_2 = '\nEu sou global!\n';

}

testFunction_2();

// console.log(globalVar_2); Não funciona porque a variável é local e não global.


if (true) {
    let x = '\nOlá mundo!\n';
    console.log(x);

}

// console.log(x); Não funciona porque a variável é local e não global.


console.log(myVar); // Vai dar como resposta undefined porque a variável não foi inicializada, mas a variável existe.
var myVar = 5;
console.log(myVar);

// Exercícios:

var idade = 25;
let nome = 'Hilário';
const pais = 'Brasil';

function mostraNome() {
    let sobreNome = 'Oliveira';
    console.log(sobreNome);

}

mostraNome();
// console.log(sobreNome); Não acessa, pois a variável é local e não global


var cidade = 'Espera Feliz';

function mostraCidade() {
    console.log(cidade);

}

mostraCidade();

if (true) {
    let bairro = 'Centro';

}

// console.log(bairro); Não acessa, pois a variável é local e não global

function testeHoisting() {
    //console.log(escola); Não funciona porque não é variável de escopo.
    let escola = 'UFOP'; 

    console.log(curso); // Funcionada porque é uma variável de escopo.
    var curso = '\nJavaScript\n'; 

}

testeHoisting();


function exemploHoisting() {
    iniciar();

}

exemploHoisting();

function iniciar() {
    console.log('\nHilário o lindo!\n');

}

iniciar();
