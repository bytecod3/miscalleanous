// Factorize a number n, e.g given 10, print 5 and 2

function primeFactorization(n){
    // print the number of twos that divide n
    while(n%2 === 0){
        console.log(2);
        n = n/2;
    }

    // n is odd at this point
    for(let i=3; i*i <n; i =i+2){
        // while i divides n, print i and divide n
        while(n%i === 0){
            console.log(i);
            n = n/i;
        }
    }

    // handle the case when n is a prime number greater than 2
    if(n > 2){
        console.log(n);
    }
}

primeFactorization(23);