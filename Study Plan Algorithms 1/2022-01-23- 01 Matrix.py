"""
From: https://leetcode.com/problems/01-matrix/
"""


from typing import Optional, Literal, Set
import itertools as it


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        self.mat = mat
        n_rows = len(mat)
        n_cols = len(mat[0])
        self.locs_to_dists: dict[tuple[int, int], int] = {}
        self.dists_to_locs: list[set[tuple[int, int]]] \
            = [set() for i in range(n_rows+n_cols)]

        # Initialize
        for row in range(n_rows):
            for col in range(n_cols):
                loc = (row, col)
                if self.mat[row][col] == 0:
                    self.locs_to_dists[loc] = 0
                    self.dists_to_locs[0].add(loc)
                else:
                    self.locs_to_dists[(row, col)] = n_rows+n_cols-1
                    self.dists_to_locs[n_rows+n_cols-1].add(loc)

        # Find distances
        for dist in range(n_rows+n_cols-1):
            for loc in self.dists_to_locs[dist]:
                row, col = loc
                neighbor_locs = []
                if row - 1 >= 0: neighbor_locs.append((row-1, col))
                if row + 1 < n_rows: neighbor_locs.append((row+1, col))
                if col - 1 >= 0: neighbor_locs.append((row, col-1))
                if col + 1 < n_cols: neighbor_locs.append((row, col+1))
                for ln in neighbor_locs:

                    distn = self.locs_to_dists[ln]
                    if distn > dist + 1:
                        self.dists_to_locs[distn].remove(ln)
                        self.dists_to_locs[dist + 1].add(ln)
                        self.locs_to_dists[ln] = dist + 1

        # Construct new matrix
        new_mat = []
        for row in range(n_rows):
            new_mat.append([self.locs_to_dists[(row, col)]
                            for col in range(n_cols)])
        return new_mat


if __name__ == "__main__":
    res = Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]])
    assert res == [[0,0,0],[0,1,0],[0,0,0]]

    res = Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
    assert res == [[0,0,0],[0,1,0],[1,2,1]]

    print(f"all done")
