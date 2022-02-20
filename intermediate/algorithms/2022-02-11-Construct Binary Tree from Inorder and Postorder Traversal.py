"""
From: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""

from __future__ import annotations

import dataclasses
from typing import Optional
import textwrap


# Definition for a binary tree node.
@dataclasses.dataclass
class TreeNode:
    val: int
    left: TreeNode = None
    right: TreeNode = None

    def __str__(self) -> str:
        indent = '\t'
        s = ""
        s += f"val: {self.val}"
        s += f"\nleft:\n{textwrap.indent(str(self.left), indent)}"
        s += f"\nright:\n{textwrap.indent(str(self.right), indent)}"
        s += f"\n"
        return s

    # def __init__(self, val=0, left=None, right=None):
    #     self.val = val
    #     self.left = left
    #     self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]
                  ) -> Optional[TreeNode]:
        if not inorder:
            assert not postorder
            return None
        root_val = postorder[-1]
        ind = inorder.index(root_val)
        left = self.buildTree(inorder[:ind], postorder[:ind])
        right = self.buildTree(inorder[ind+1:], postorder[ind:-1])
        return TreeNode(root_val, left, right)


if __name__ == "__main__":

    tree = Solution().buildTree(inorder = [9,3,15,20,7],
                             postorder = [9,15,7,20,3])
    print(f"\n tree is [[\n{tree}\n]]")

    print(f"all done")
