"""
From: https://leetcode.com/problems/reverse-integer/
"""

class Solution:
    def reverse(self, x: int) -> int:
        # return self.reverse_str(x)
        return self.reverse_no_str(x)

    def reverse_str(self, x: int) -> int:
        xs = str(x)

        if xs.startswith("-"):
            sign = "-"
            num = xs[1:]
        else:
            sign = ""
            num = xs

        xs_reversed = sign + num[::-1]

        # Check won't be too big
        # -2^31 <= x <= 2^31 - 1
        if xs_reversed.startswith("-"):
            big_digit = xs_reversed[1]
            rest = xs_reversed[2:]
            start = 2**31
        else:
            big_digit = xs_reversed[0]
            rest = xs_reversed[1:]
            start = 2**31-1

        if rest:
            to_sub = [int('1'+'0'*len(rest))]*int(big_digit) + [int(rest)]
            for n in to_sub:
                start -= n
                if start < 0:
                    return 0  # It's too big

        res = int(xs_reversed)
        return res

    def reverse_no_str(self, x: int) -> int:
        xa = abs(x)
        xr = 0
        limit = 2**31 if x < 0 else 2**31 - 1
        while xa:
            xa, digit = divmod(xa, 10)
            print(f" xa, digit is [[{xa, digit}]]")
            if xr > (limit - digit) // 10:
                return 0
            xr = xr*10 + digit
        if x < 0:
            xr *= -1
        return xr

if __name__ == "__main__":
    res = Solution().reverse(123)
    assert res == 321

    res = Solution().reverse(-123)
    assert res == -321

    res = Solution().reverse(-120)
    assert res == -21

    res = Solution().reverse(2147483647)
    assert res == 0

    res = Solution().reverse(2147483642)
    assert res == 0

    res = Solution().reverse(2147483641)
    assert res == 1463847412

    res = Solution().reverse(-2147483648)
    assert res == 0

    res = Solution().reverse(-2147483642)
    assert res == 0

    res = Solution().reverse(-2147483641)
    assert res == -1463847412

    res = Solution().reverse(-2047483641)
    assert res == -1463847402

    res = Solution().reverse(-2)
    assert res == -2

    print(2**31)

    print(f"All done")