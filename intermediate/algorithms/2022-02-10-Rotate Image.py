"""
From: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""

import math


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        assert len(matrix) == len(matrix[0])
        d = len(matrix)

        for row in range(d//2):
            for col in range(math.ceil(d/2)):
                matrix[row][col], matrix[col][d-1-row], \
                matrix[d-1-row][d-1-col], matrix[d-1-col][row] \
                    = matrix[d-1-col][row], matrix[row][col], \
                      matrix[col][d-1-row], matrix[d-1-row][d-1-col]


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(m)
    assert m == [[7,4,1],[8,5,2],[9,6,3]]

    m = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    Solution().rotate(m)

    m = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    Solution().rotate(m)
    assert m == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    print(f"all done")
