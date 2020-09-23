// optimized function to check prime numbers
// 1) all prime numbers are in the form 6k (+-) 1
// 2) if the square root of n is not a prime number, the
//   number n is not a prime number by definition

function isPrime(n){
    if(n <= 1) return false;
    if(n <= 3) return true;

    // this is checked to skip
    //the middle five numbers in below loop
    if (n%2 === 0 || n%3 ===0) return false;

    for(let i=5; i*i<=n; i=i+6){

        if(n%i === 0 || n%(i+2) === 0){
            return false;
        }
    }

    return true;
}