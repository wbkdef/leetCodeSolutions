


/**
 * @param {number} num
 * @return {boolean}
 */
function isPalindrome(num) {
  sn = num.toString();
  for (let i = 0; i < sn.length/2; i++) {
    if (sn[i] !== sn[sn.length-i-1]) {
      return false;
    };
  };
  return true;
};


console.log("isPalindrome(121)", isPalindrome(121))

console.log("isPalindrome(12321)", isPalindrome(12321))
console.log("isPalindrome(1221)", isPalindrome(1221))

console.log("isPalindrome(123)", isPalindrome(123))
console.log("isPalindrome(123521)", isPalindrome(123521))