"""
From: https://leetcode.com/problems/single-number-ii/
"""

from __future__ import annotations

import copy
import itertools as it
import math
from typing import Optional
import textwrap
import dataclasses
import functools
import pprint


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        once = 0
        twice = 0
        for n in nums:
            assert once & twice == 0
            zero_times = ~(once | twice)
            twice = (twice & ~n) | (once & n)
            once = (once & ~n) | (zero_times & n)

            # print(f"After {n}, {once=}, {twice=}")

        assert twice == 0
        return once


if __name__ == "__main__":
    res = Solution().singleNumber([2,2,3,2])
    assert res == 3

    res = Solution().singleNumber([20,20,38,20])
    assert res == 38

    res = Solution().singleNumber([-20,-20,38,-20])
    assert res == 38

    res = Solution().singleNumber([0,1,0,1,0,1,99])
    assert res == 99

    res = Solution().singleNumber([0, -21, 0, -21, 0, -21, -21, 99, -21, -21])
    assert res == 99

    print(f"all done")
