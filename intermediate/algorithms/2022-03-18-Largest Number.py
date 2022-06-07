"""
From: https://leetcode.com/problems/largest-number/
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

# def sk():


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        if not nums:
            return ""

        nss = sorted((str(n) for n in nums), key=lambda n: n+'a', reverse=True)
        print(f" nss is [[{nss}]]")

        extra = nss[0]
        res = []

        for i in range(1, len(nss)):
            if nss[i].startswith(extra):
                if nss[i] == extra:
                    res.append(nss[i])
                else:
                    if nss[i][len(extra):] > extra:
                        res.append(nss[i])
                    elif nss[i][len(extra):] < extra:
                        res.append(extra)
                        extra = nss[i]
                    else:
                        pass
                        #todo
            else:
                if extra > nss[i]:
                    res.append(extra)
                    extra = nss[i]
                else:
                    res.append(nss[i])
        res.append(extra)
        print(f" res is [[{res}]]")
        return "".join(res)

        print(f"done largestNumber")


if __name__ == "__main__":
    # res = Solution().largestNumber([10,2])
    # assert res == "210"

    res = Solution().largestNumber([3,30,34,5,9])
    assert res == "9534330"

    res = Solution().largestNumber([3,30,32,5,9])
    assert res == "9533230"

    res = Solution().largestNumber([36,360,362,5,9])
    assert res == "9536362360"

    res = Solution().largestNumber([36,360,364,5,9])
    assert res == "9536436360"

    print(f"all done")
