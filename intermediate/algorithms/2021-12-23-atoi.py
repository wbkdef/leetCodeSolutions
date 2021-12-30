"""
From: https://leetcode.com/problems/string-to-integer-atoi/
"""

import re


class Solution:
    def myAtoi(self, s: str) -> int:
        sp = s.strip()

        if not sp:
            return 0
        sign = 1
        if sp[0] == "-":
            sign = -1
        if sp[0] in "-+":
            sp = sp[1:]

        m = re.search(r"^\d+", sp, flags=re.MULTILINE | re.DOTALL)
        # val = int(m.group()) * sign
        if m:
            val = int(m.group()) * sign
        else:
            val = 0

        # [-231, 231 - 1]
        val = max(val,  -2**31)
        val = min(val,  2**31 - 1)

        return val


if __name__ == "__main__":
    res = Solution().myAtoi("42")
    assert res == 42

    res = Solution().myAtoi("   -42")
    assert res == -42

    res = Solution().myAtoi("4193 with words")
    assert res == 4193

    res = Solution().myAtoi("  +2147483647bla")
    assert res == 2147483647

    res = Solution().myAtoi("  +2147483849bla")
    assert res == 2147483647

    res = Solution().myAtoi("  -2147483648bla")
    assert res == -2147483648

    res = Solution().myAtoi("  -2148483648bla")
    assert res == -2147483648

    res = Solution().myAtoi("  -bla")
    assert res == -0

    res = Solution().myAtoi("  ")
    assert res == -0

    print(f"All done")