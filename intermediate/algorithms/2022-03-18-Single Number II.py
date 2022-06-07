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


#  todo:  Fix so works for -ve numbers

import itertools as it
def to_reverse_base_3(num: int)  ->  list[int]:
    n = abs(num)
    base3 = [0] if num >= 0 else [1]
    while n:
        n, m = divmod(n, 3)
        base3.append(m)

    # print(f"num:{num} converted to {base3} in base 3")
    return base3


def reverse_base_3_to_num(base3: list[int])  ->  int:
    s = 0
    for i, d in enumerate(base3[1:]):
        s += d*3**i

    assert base3[0] in (0, 1)
    if base3[0] == 1:
        s = -s
    # print(f"base3:{base3} converted to {s}")
    return s


def base3_xor(num1: list[int], num2: list[int])  ->  list[int]:
    new_num = []
    for n1, n2 in it.zip_longest(num1, num2):
        if n1 is None:
            n1 = 0
        if n2 is None:
            n2 = 0
        res = (n1 + n2) % 3
        new_num.append(res)
    # print(f"base3_xor: {num1}^{num2} = {new_num}")
    return new_num


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        base3 = []
        for n in nums:
            base3 = base3_xor(to_reverse_base_3(n), base3)

        res = reverse_base_3_to_num(base3)
        return res



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
