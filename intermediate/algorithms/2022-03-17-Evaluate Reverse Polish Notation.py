"""
From: https://leetcode.com/problems/evaluate-reverse-polish-notation/
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
    def evalRPN(self, tokens: list[str]) -> int:
        tc = copy.copy(tokens)
        # print(f"\n----")
        # print(f"tc is now {tc}")
        i = 0
        while i < len(tc):
            # print(f" i is [[{i}]]")
            if tc[i] in "+-*/":

                v1 = int(tc[i - 2])
                v2 = int(tc[i - 1])
                if tc[i] == "+": res = v1 + v2
                elif tc[i] == "-": res = v1 - v2
                elif tc[i] == "*": res = v1 * v2
                elif tc[i] == "/":
                    res = v1 / v2
                    if res > 0:
                        res = math.floor(res)
                    elif res < 0:
                        res = math.ceil(res)
                    else:
                        res = int(res)
                tc[i-2:i+1] = [res]
                i -= 1
                # print(f"tc is now {tc}")
            else:
                i += 1

        assert len(tc) == 1
        return tc[0]


if __name__ == "__main__":
    res = Solution().evalRPN(["2", "1", "+", "3", "*"])
    assert res == 9

    res = Solution().evalRPN(["4","13","5","/","+"])
    assert res == 6

    res = Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    assert res == 22

    res = Solution().evalRPN(["0","3","/"])
    assert isinstance(res, int)
    assert res == 0

    print(f"all done")
