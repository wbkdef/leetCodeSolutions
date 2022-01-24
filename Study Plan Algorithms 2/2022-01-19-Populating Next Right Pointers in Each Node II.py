"""
From: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0,
                 left: 'Node' = None, right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        s = f"val: {self.val}"
        s += f"\nleft:\n{self.left}"
        s += f"\nright:\n{self.right}"
        s += f"\nnext: {self.next}"
        return s

    def __eq__(self, other):
        return all([
            self.val == other.val,
            self.left == other.left,
            self.right == other.right,
            self.next == other.next,
        ])

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        layer = [root]

        while layer:
            next_layer = []
            next_node = None
            for node in layer:
                if node.right:
                    next_layer.append(node.right)
                if node.left:
                    next_layer.append(node.left)
                node.next = next_node
                next_node = node
            layer = next_layer

        return root


if __name__ == "__main__":

    root = Node(
        1,
        Node(
            2,
            Node(4),
            Node(5),
        ),
        Node(
            3,
            None,
            Node(7),
        ),
    )
    res = Solution().connect(root)
    print()
    print(res)
    # assert res == 1

    res = Solution().connect(None)
    assert res == None

    res = Solution().connect(Node(5))
    print()
    print(res)
    assert res == Node(5)

    print(f"all done")
