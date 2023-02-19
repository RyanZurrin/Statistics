

// create javascript object that will hold a dictionary of words loaded from a txt file
let words = {};
let permutations = [];

// load the words from the txt file into the words object
$.get('words.txt', function(data) {
    let lines = data.split('\n');
    for (let i = 0; i < lines.length; i++) {
        let word = lines[i].split(' ');
        words[word[0]] = word[1];
    }
    // display the words object in the console
    console.log(words);
});

// function to find all permutations of a string under 20 characters
function permute(str) {
    let arr = str.split(''),
        len = arr.length,
        perms = [],
        rest,
        picked,
        restPerms,
        next;

    if (len == 0)
        return [str];

    for (let i = 0; i < len; i++) {
        rest = Object.create(arr);
        picked = rest.splice(i, 1);

        restPerms = permute(rest.join(''));

        for (let j = 0, jLen = restPerms.length; j < jLen; j++) {
            next = picked.concat(restPerms[j]);
            perms.push(next.join(''));
        }
    }
    return perms;
}

// isWord function to check if a string is a word in the words object
function isWord(str) {
    return words.hasOwnProperty(str);
}

// function given a list of permutations, return a list of valid words with no duplicates
function getWords(perms) {
    let words = [];
    for (let i = 0; i < perms.length; i++) {
        if (isWord(perms[i])) {
            words.push(perms[i]);
        }
    }
    return words;
}

// when the html page is loaded fill the words object with the words from the txt file
$(document).ready(function() {
    // automatically load the word list into the words object
    $.get('js/words.txt', function(data) {
        let lines = data.split('\n');
        for (let i = 0; i < lines.length; i++) {
            let word = lines[i].split(' ');
            words[word[0]] = word[1];
        }
        // display the words object in the console
        console.log(words);
    });
});
