


/**
 * @param {string} s
 * @return {number}
 */
function romanToInt(s) {
    sm = s;
    sm = sm.replace('IV', 'IIII');
    sm = sm.replace('IX', 'VIIII');
    sm = sm.replace('XL', 'XXXX');
    sm = sm.replace('XC', 'LXXXX');
    sm = sm.replace('CD', 'CCCC');
    sm = sm.replace('CM', 'DCCCC');

    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000};

    let val = 0;
    for (const key in numerals) {
      console.log('key is: ', key)
      val += numerals[key] * (sm.split(key).length - 1);
    }

    return val
};

console.log('III: ', romanToInt('III'))
console.log('LVIII: ', romanToInt('LVIII'))
console.log('MCMXCIV: ', romanToInt('MCMXCIV'))
