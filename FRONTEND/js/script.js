// create javascript object that will hold a dictionary of words loaded from a txt file
let words = {};
let permutations = [];
let perms = [];
// load the words from the txt file into the words object


// make all the functions available to the HTML page


$.get('js/words.txt', function (data) {
    // log to console that the words.txt file was loaded
    console.log('words.txt file loaded');
    let lines = data.split('\n');
    for (let i = 0; i < lines.length; i++) {
        let word = lines[i].split(' ');
        words[word[0]] = word[1];
    }
    // display the words object in the console
    console.log(words);
});

// funciton to validate the input is uncer 15 characters and only contains letters and spaces
function validate(str) {
    let regex = /^[a-zA-Z\s]*$/;
    if (str.length > 15 || !regex.test(str)) {
        return false;
    } else {
        return true;
    }
}

// function to find all permutations of a string
function permute(str, len) {
    // log to console in permute function was hit
    console.log('permute function hit');
    let arr = str.split('');
    if (len === undefined) {
        len = arr.length;
    }
    if (len === 1) {
        return arr.map(function (val) {
            return val;
        });
    }
    for (let i = 0; i < arr.length; i++) {
        let firstChar = arr.splice(i, 1);
        let innerPerms = permute(arr.join(''), len - 1);
        for (let j = 0; j < innerPerms.length; j++) {
            perms.push(firstChar + innerPerms[j]);
        }
        arr.splice(i, 0, firstChar);
    }
    return perms;
}


// function to find all arrangemntes of a string so a 4 letter word will have 64 different permutations
// whiich is 4C1 + 4C2 + 4C3 + 4C4
function allArrangements(str) {
    // log to console in allArrangements function was hit
    console.log('allArrangements function hit');
    for (let i = 1; i <= str.length; i++) {
        perms = perms.concat(permute(str, i));
    }
    return perms;
}

// isWord function to check if a string is a word in the words object
function isWord(str) {
    return words.hasOwnProperty(str);
}

// function given a list of permutations, return a list of valid words with no duplicates
function getWords(perms) {
    // log to console in getWords function was hit
    console.log('getWords function hit');
    let words = [];
    for (let i = 0; i < perms.length; i++) {
        if (isWord(perms[i])) {
            words.push(perms[i]);
        }
    }
    return words;
}

// function that when submit button is hit will use the input from the text box to find all permutations of the string
// and then find all valid words from the permutations and display them on the webpage
function submitNameHit() {
    // log to console saying submit button was hit
    console.log('submit button hit');
    let str = document.getElementById('name').value;
    let perms = allArrangements(str);
    let words = getWords(perms);
    let html = '';
    for (let i = 0; i < words.length; i++) {
        html += words[i] + '<br>';
    }
    document.getElementById('output').innerHTML = html;
    // display the words to console too
    console.log(words);
}