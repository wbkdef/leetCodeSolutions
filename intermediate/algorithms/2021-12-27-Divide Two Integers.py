"""
From: https://leetcode.com/problems/divide-two-integers/
PC:KEYfLv3:

Didn't get this one
"""

import math


# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
#             sgn = 1
#         else:
#             sgn = -1
#         unsigned = \
#             int(2 ** (math.log2(abs(dividend)) - math.log2(abs(divisor))))
#         return unsigned if sgn > 0 \
#             else -unsigned
#
#
# if __name__ == "__main__":
#     res = Solution().divide(dividend=10, divisor=3)
#     assert res == 3
#
#     res = Solution().divide(dividend=7, divisor=-3)
#     assert res == -2
#
#     print(f"All done")


def multiply(i: int, j: int):
    to_sum = []
    for n_zeros, digit in enumerate(reversed(str(i))):
        digit_js = 0
        for _ in range(int(digit)):
            digit_js += j

        zeros = ''.join('0' for i in range(n_zeros))
        to_sum.append(int(str(digit_js) + zeros))
    print(f"{to_sum=}")
    return sum(to_sum)


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sgn = 1
        else:
            sgn = -1

        remainder = abs(dividend)
        divisor = abs(divisor)
        quotient = ''

        for n_zeros in range(len(str(dividend))-len(str(divisor)), -1, -1):
            # print(n_zeros)
            divisor_with_0s = multiply(divisor, 10**n_zeros)
            for mult_by in range(9, 0, -1):
                div_mult = multiply(divisor_with_0s, mult_by)
                if div_mult <= remainder:
                    quotient += str(mult_by)
                    remainder -= div_mult
                    break
        assert remainder < divisor
        assert multiply(quotient, divisor) + remainder == abs(dividend), \
            (multiply(quotient, divisor) + remainder, abs(dividend))

        if quotient == "":
            int_q = 0
        else:
            int_q = int(quotient)

        ret = int_q if sgn > 0 else -int_q

        if ret < -2**31:
            ret = -2**31
        if ret > 2**31-1:
            ret = 2**31-1

        return ret


if __name__ == "__main__":
    assert multiply(3, 4) == 12
    assert multiply(12, 14) == 168

    assert Solution().divide(1248, 11) == 1248//11
    assert Solution().divide(1248, -13) == 1248 // -13
    assert Solution().divide(124, -130) == 0

    print(f"all done")
