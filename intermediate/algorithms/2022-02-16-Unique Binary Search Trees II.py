"""
From: https://leetcode.com/problems/unique-binary-search-trees-ii/
"""

from __future__ import annotations
from typing import Optional
import functools
import textwrap

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        s = f"val: {self.val}"
        left = textwrap.indent(str(self.left), "    ")
        s += f"\n left:\n{left}"
        right = textwrap.indent(str(self.right), "    ")
        s += f"\n right:\n{right}"
        return s


class Solution:
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        if n < 1:
            return [None]

        return self.generateTrees_(1, n)

    @functools.cache
    def generateTrees_(self, ind_start: int, ind_end: int) -> list[Optional[TreeNode]]:
        if ind_start > ind_end:
            return [None]
        if ind_start == ind_end:
            return [TreeNode(ind_start)]
        assert ind_start < ind_end

        trees = []
        for ind in range(ind_start, ind_end + 1):
            for tree_left in self.generateTrees_(ind_start, ind - 1):
                for tree_right in self.generateTrees_(ind + 1, ind_end):
                    trees.append(TreeNode(ind, tree_left, tree_right))
        return trees


if __name__ == "__main__":
    res = Solution().generateTrees(1)
    assert len(res) == 1
    print(f"\n res is [[\n{res}\n]]")

    res = Solution().generateTrees(2)
    assert len(res) == 2
    print(f"\n res is [[\n{res}\n]]")

    res = Solution().generateTrees(3)
    assert len(res) == 5
    print(f"\n res is [[\n{res}\n]]")

    print(f"all done")
