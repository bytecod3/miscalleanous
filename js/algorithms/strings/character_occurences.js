// return the number of times a character appears in a string

function noOfChars(str, char){
    let count = 0;
    let pos = str.indexOf(char);
    while(pos !== -1){
        count++;
        pos = str.indexOf(char, pos+1);
    }

    return count;
}


console.log(noOfChars('eddwind', 'd'));
