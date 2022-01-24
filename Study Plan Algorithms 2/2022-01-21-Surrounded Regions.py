"""
From: https://leetcode.com/problems/surrounded-regions/
"""


from typing import Optional, Literal, Set


class Solution:
    def get(self, loc: tuple[int, int]):
        row, col = loc
        return self.board[row][col]

    def set(self, loc: tuple[int, int], val: Literal['X', 'O']):
        row, col = loc
        self.board[row][col] = val

    def get_neighbors(self, loc: tuple[int, int])  ->  list[tuple[int, int]]:
        row, col = loc
        neighbors = []
        for row2, col2 in [(row+1, col), (row-1, col),
                           (row, col+1), (row, col-1)]:
            if 0 <= row2 < self.n_rows:
                if 0 <= col2 < self.n_cols:
                    neighbors.append((row2, col2))
        return neighbors

    def get_connected_locs(self, loc: tuple[int, int]) -> Set[tuple[int, int]]:
    # def get_connected_locs(self, loc):
        frontier = [loc]
        connected_locs = set()
        while frontier:
            loc = frontier.pop(0)
            if self.get(loc) == 'X' or loc in connected_locs:
                continue
            assert self.get(loc) == 'O'

            connected_locs.add(loc)
            frontier.extend(self.get_neighbors(loc))
        return connected_locs

    def patch_touches_edge(self, locs: Set[tuple[int, int]])  ->  bool:
        for row, col in locs:
            if row in [0, self.n_rows-1] or \
                    col in [0, self.n_cols - 1]:
                return True
        return False

    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.n_rows = len(board)
        if not self.n_rows:
            return
        self.n_cols = len(board[0])

        self.explored_locs = set()  # tuple[row, col]
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                loc = (row, col)
                val = self.get(loc)
                if loc in self.explored_locs or val == 'X':
                    self.explored_locs.add(loc)
                    continue

                assert val == 'O'

                locs = self.get_connected_locs(loc)
                touches = self.patch_touches_edge(locs)
                print(f"\n locs is [[\n{locs}\n]]")
                for loc2 in locs:
                    self.explored_locs.add(loc2)
                    if not touches:
                        self.set(loc2, 'X')


if __name__ == "__main__":
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    Solution().solve(board)
    assert board == [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

    board = [["X"]]
    Solution().solve(board)
    assert board == [["X"]]

    print(f"all done")
