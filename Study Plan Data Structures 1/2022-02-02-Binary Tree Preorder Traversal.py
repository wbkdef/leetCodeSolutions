"""
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        """ Doing the iterative solution as a challenge """
        if not root:
            return None

        to_traverse = [root]
        res = []
        while to_traverse:
            node = to_traverse.pop()
            res.append(node.val)
            if node.right:
                to_traverse.append(node.right)
            if node.left:
                to_traverse.append(node.left)

        return res


if __name__ == '__main__':
    tree = TreeNode(1, None,
                    TreeNode(2,
                             TreeNode(3)))
    res = Solution().preorderTraversal(tree)
    assert res == [1, 2, 3]

    print(f"done")
