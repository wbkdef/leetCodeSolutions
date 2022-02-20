"""
From: https://leetcode.com/problems/interleaving-string/
"""

from __future__ import annotations

import itertools as it
from typing import Optional
import textwrap
import dataclasses
import functools
import pprint


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        sols = []
        for i2 in range(len(s2)+1):
            sols.append([])
            for i1 in range(len(s1)+1):
                if i1 == i2 == 0:
                    sols[i2].append(True)
                elif i2 > 0 and sols[i2-1][i1] is True and s2[i2-1] == s3[i1+i2-1]:
                    sols[i2].append(True)
                elif i1 > 0 and sols[i2][i1-1] is True and s1[i1-1] == s3[i1+i2-1]:
                    sols[i2].append(True)
                else:
                    sols[i2].append(False)

        # pprint.pprint(sols)
        return sols[-1][-1]





if __name__ == "__main__":
    res = Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac")
    assert res is True

    res = Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc")
    assert res is False

    res = Solution().isInterleave(s1 = "", s2 = "", s3 = "")
    assert res is True

    res = Solution().isInterleave(s1 = "", s2 = "", s3 = "a")
    assert res is False

    print(f"all done")
