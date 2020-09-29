// test whether a number is prime
function isPrime(n){
    if( n <= 1){
        //the first prime number is 2
        return false;
    }

    // check from 2 to n-1
    for (let i=2; i < n; i++){
        if (n%i === 0){
            return false;
        }
    }

    // else the number must be even
    return true;
}

console.log(isPrime(11));

