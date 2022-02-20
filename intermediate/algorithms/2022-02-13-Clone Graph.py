"""
From: https://leetcode.com/problems/clone-graph/
"""

from __future__ import annotations


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_nodes: dict[int, 'Node'] = {}

        to_explore: list['Node'] = [node]
        while to_explore:
            n = to_explore.pop()
            old_nodes[n.val] = n
            for nn in n.neighbors:
                if nn.val not in old_nodes:
                    to_explore.append(nn)

        new_nodes: dict[int, 'Node'] = {val: Node(val) for val in old_nodes}
        for val in new_nodes:
            old_n = old_nodes[val]
            new_n = new_nodes[val]
            for old_neighbor in old_n.neighbors:
                old_neighbor_val = old_neighbor.val
                new_n.neighbors.append(new_nodes[old_neighbor_val])

        return new_nodes[node.val]


if __name__ == "__main__":
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]
    cg1 = Solution().cloneGraph(n1)
    assert not n1 is cg1
    assert {n.val for n in cg1.neighbors} == {2, 4}
    cg2, = {n for n in cg1.neighbors if n.val == 2}
    assert {n.val for n in cg2.neighbors} == {1, 3}

    print(f"all done")
