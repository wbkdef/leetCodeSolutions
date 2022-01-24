"""
From: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(
            self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:
        if self.are_equal(root, subRoot):
            return True
        if root.left and self.isSubtree(root.left,  subRoot):
            return True
        if root.right and self.isSubtree(root.right,  subRoot):
            return True
        return False

    def are_equal(
            self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    )  ->  bool:
        if root1 == root2:
            # Case both are None, or is the same tree
            return True
        if None in [root1, root2]:
            # Case only one is None
            return False
        if root1.val != root2.val:
            return False
        if not self.are_equal(root1.left, root2.left):
            return False
        if not self.are_equal(root1.right, root2.right):
            return False
        return True

if __name__ == "__main__":


    print(f"all done")
