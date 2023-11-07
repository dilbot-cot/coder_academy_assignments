/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    // first if the number is odd, return false, except if n = 1
    if (n % 2 == 0 || n == 1) {
        
        // while loop as long as 'i' is less than 'n'
        let i = 0
        while (i <= n){
            // Math operation to determine the power
            let result = Math.pow(2,i)
            // if result == n return true
            if (result == n){
                return true
            // check if the result is less than n, and increment i by 1
            } else if (result < n){
                i +=1
            // failing both conditions, return false
            } else {
                return false
            }
        }
        // handles negative numbers as i will be greater than n
        return false;

    // return false if the number is odd, as can never be a power of two
    } else {
        return false;
    }
};