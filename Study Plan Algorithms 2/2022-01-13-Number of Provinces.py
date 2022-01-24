"""
From: https://leetcode.com/problems/number-of-provinces/submissions/
"""

from typing import Optional


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        self.is_connected = isConnected
        n_nodes = len(isConnected)

        nodes_not_assigned = set(range(n_nodes))
        n_provinces = 0
        while nodes_not_assigned:
            n_provinces += 1
            province = self.get_nodes_connected_to(next(iter(nodes_not_assigned)))
            print(f" province is [[{province}]]")
            assert province.issubset(nodes_not_assigned)
            nodes_not_assigned -= province

        return n_provinces

    def get_nodes_connected_to(self, node: int)  ->  set[int]:
        nodes_frontier = [node]
        nodes_explored = set()
        while nodes_frontier:
            node = nodes_frontier.pop()
            nodes_explored.add(node)
            for j in range(len(self.is_connected)):
                if self.is_connected[node][j] and j not in nodes_explored:
                    nodes_frontier.append(j)
        return nodes_explored


if __name__ == "__main__":
    # res = Solution().findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]])
    # assert res == 2
    #
    # res = Solution().findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]])
    # assert res == 3

    res = Solution().findCircleNum(isConnected = [[1,1,0],[1,1,1],[0,1,1]])
    assert res == 1

    print(f"all done")
