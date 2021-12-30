"""
From: https://leetcode.com/problems/integer-to-roman/
PC:KEYeamH:
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        n = num
        s = ''

        Ms, n = divmod(n, 1000)
        s += 'M' * Ms

        Ds, n = divmod(n, 500)
        s += 'D' * Ds

        Cs, n = divmod(n, 100)
        s += 'C' * Cs

        Ls, n = divmod(n, 50)
        s += 'L' * Ls

        Xs, n = divmod(n, 10)
        s += 'X' * Xs

        Vs, n = divmod(n, 5)
        s += 'V' * Vs
        s += 'I' * n

        s = s.replace('DCCCC', 'CM')
        s = s.replace('CCCC', 'CD')
        s = s.replace('LXXXX', 'XC')
        s = s.replace('XXXX', 'XL')
        s = s.replace('VIIII', 'IX')
        s = s.replace('IIII', 'IV')

        return s

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

if __name__ == "__main__":
    res = Solution().intToRoman(3)
    assert res == "III"

    res = Solution().intToRoman(58)
    assert res == "LVIII"

    res = Solution().intToRoman(1994)
    'MDCCCCLXXXXIIII'
    'MCM   LXXXXIIII'
    'MCM   XC   IIII'
    'MCM   XC   IV'
    assert res == "MCMXCIV"

    print(f"All done")