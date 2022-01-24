"""
From: https://leetcode.com/problems/01-matrix/
"""


from typing import Optional, Literal, Set
import itertools as it


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


if __name__ == "__main__":
    res = Solution().singleNumber([2,2,1])
    assert res == 1

    res = Solution().singleNumber([4,1,2,1,2])
    assert res == 4

    res = Solution().singleNumber([3])
    assert res == 3

    print(f"all done")
