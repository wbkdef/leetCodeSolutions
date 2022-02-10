"""
From: https://leetcode.com/problems/spiral-matrix
"""

from typing import Iterable


def spiral_order(n_rows, n_cols)  ->  Iterable[tuple[int, int]]:
    """ yields (row, col) """
    row_min = 0
    row_max = n_rows-1
    col_min = 0
    col_max = n_cols-1
    row, col = 0, 0
    while True:
        # top row going right
        if col_min > col_max:
            break
        for col in range(col_min, col_max+1):
            yield row, col
        row_min += 1

        # right col going down
        if row_min > row_max:
            break
        for row in range(row_min, row_max+1):
            yield row, col
        col_max -= 1

        # bottom row going left
        if col_min > col_max:
            break
        for col in range(col_max, col_min-1, -1):
            yield row, col
        row_max -= 1

        # bottom row going left
        if row_min > row_max:
            break
        for row in range(row_max, row_min-1, -1):
            yield row, col
        col_min += 1



class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []
        ret = []
        for row, col in spiral_order(len(matrix), len(matrix[0])):
            ret.append(matrix[row][col])
        return ret

if __name__ == "__main__":
    assert Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])\
           == [1,2,3,6,9,8,7,4,5]
    assert Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])\
           == [1,2,3,4,8,12,11,10,9,5,6,7]

    print(f"all done")
