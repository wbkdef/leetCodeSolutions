"""
From: https://leetcode.com/problems/power-of-two/
"""


from typing import Optional, Literal, Set
import itertools as it


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        br = n & (n - 1)
        print(f" br is [[{br}]]")
        if br == 0:
            return True
        return False


if __name__ == "__main__":
    res = Solution().isPowerOfTwo(1)
    assert res == True

    res = Solution().isPowerOfTwo(16)
    assert res == True

    res = Solution().isPowerOfTwo(3)
    assert res == False

    res = Solution().isPowerOfTwo(-4)
    assert res == False

    res = Solution().isPowerOfTwo(-3)
    assert res == False

    print(f"all done")
