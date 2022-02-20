"""
From: https://leetcode.com/problems/interleaving-string/
"""

from __future__ import annotations

import itertools as it
from typing import Optional
import textwrap
import dataclasses
import functools


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str, i1: int = 0, i2: int = 0) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        self.s1: str = s1
        self.s2: str = s2
        self.s3: str = s3
        return self.isInterleave_(0, 0)

    functools.cache
    def isInterleave_(self, i1: int = 0, i2: int = 0) -> bool:
        s1, s2, s3 = self.s1, self.s2, self.s3

        i = i1 + i2
        if i == len(s3):
            return True

        if i1 == len(s1):
            if s2[i2] == s3[i]:
                return self.isInterleave_(i1, i2+1)
            else:
                return False

        if i2 == len(s2):
            if s1[i1] == s3[i]:
                return self.isInterleave_(i1+1, i2)
            else:
                return False

        if s1[i1] == s3[i] and self.isInterleave_(i1+1, i2):
            return True
        if s2[i2] == s3[i] and self.isInterleave_(i1, i2+1):
            return True
        return False


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
