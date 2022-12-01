'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    var vowelCharacters = '';
    var nonVowelCharacters = '';
    var vowels = ['a', 'e', 'i', 'o', 'u'];
    Array.from(s).forEach(function (character) {
        if (vowels.indexOf(character) != -1) {
            console.log(character);
        }
    });
    Array.from(s).forEach(function (character){
        if (vowels.indexOf(character) == -1) {
            console.log(character);
        }
    });
}

