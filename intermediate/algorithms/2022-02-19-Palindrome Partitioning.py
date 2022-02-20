"""
From: https://leetcode.com/problems/palindrome-partitioning/
"""

from __future__ import annotations

import itertools as it
from typing import Optional
import textwrap
import dataclasses
import functools
import pprint


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        self.s = s
        all_partitions = [[[]]]
        for i_end in range(1, len(s) + 1):
            all_partitions.append([])
            for i_start in range(i_end):
                if self.is_palindrome(i_start, i_end):
                    last_palindrome = s[i_start: i_end]
                    for partition in all_partitions[i_start]:
                        all_partitions[-1].append(partition + [last_palindrome])

        # print()
        # print(s)
        # for p in all_partitions:
        #     print(p)
        return all_partitions[-1]

    def is_palindrome(self, start_ind, end_ind):
        """ Looking at s[start_ind: end_ind] """
        for i in range((end_ind - start_ind)//2):
            if self.s[start_ind + i] != self.s[end_ind - i - 1]:
                return False
        return True


if __name__ == "__main__":
    res = Solution().partition("aab")
    assert res == [["aa","b"],["a","a","b"]]

    res = Solution().partition("abab")
    assert res == [["a", "bab"], ["aba","b"], ["a","b","a", "b"]]

    res = Solution().partition("a")
    assert res == [["a"]]

    print(f"all done")
