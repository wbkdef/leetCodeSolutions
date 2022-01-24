"""
From: https://leetcode.com/problems/shortest-path-in-binary-matrix/submissions/
"""


from typing import Optional


class Solution:
    def get(self, loc: tuple[int, int])  ->  int:
        assert 0 <= loc[0] < self.n
        assert 0 <= loc[1] < self.n
        return self.grid[loc[0]][loc[1]]

    def get_neighbors(self, loc: tuple[int, int])  ->  set[tuple[int, int]]:
        y, x = loc
        locs = set()
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx != 0 or dy != 0:
                    x2 = x + dx
                    y2 = y + dy
                    if 0 <= x2 < self.n and 0 <= y2 < self.n:
                        locs.add((y2, x2))
        return locs

    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        self.grid = grid
        self.n = len(grid)

        frontier = [((0, 0), 1)]
        explored = {}
        while frontier:
            print(f" frontier is [[{frontier}]]")
            loc, dist = frontier.pop(0)

            if self.get(loc) != 0:
                continue
            if loc == (self.n-1, self.n-1):
                print(f"\n explored is [[\n{explored}\n]]")
                return dist

            if loc not in explored:
                explored[loc] = dist
            else:
                assert dist >= explored[loc]
                continue

            frontier.extend([(ln, dist+1) for ln in self.get_neighbors(loc)])

        print(f"\n explored is [[\n{explored}\n]]")
        return -1


if __name__ == "__main__":
    res = Solution().shortestPathBinaryMatrix([[0, 1], [1, 0]])
    assert res == 2

    res = Solution().shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]])
    assert res == -1

    res = Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])
    assert res == 4

    print(f"all done")
