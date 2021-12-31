"""
From: https://leetcode.com/problems/search-a-2d-matrix/submissions/
PC:KEYsarg:
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        self.matrix = matrix
        self.target = target
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])
        assert self.n_rows > 0
        if self.n_cols == 0:
            return False

        return self.searchMatrix_(0, self.n_rows*self.n_cols-1)

    def get_at(self, ind):
        row, col = divmod(ind, self.n_cols)
        return self.matrix[row][col]

    def searchMatrix_(self, ind_min: int, ind_max: int) -> bool:
        if self.target == self.get_at(ind_min): return True
        if self.target == self.get_at(ind_max): return True
        if ind_max <= ind_min + 1:
            return False

        ind_mid = (ind_min + ind_max)//2
        val_mid = self.get_at(ind_mid)
        if self.target == val_mid: return True
        elif self.target < val_mid: return self.searchMatrix_(ind_min, ind_mid)
        elif self.target > val_mid: return self.searchMatrix_(ind_mid, ind_max)
        else:
            assert False


if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    res = Solution().searchMatrix(matrix, target)
    assert res == True

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    res = Solution().searchMatrix(matrix, target)
    assert res == False

    matrix = [[13, 23, 25, 27], [210, 211, 216, 220], [223, 230, 234, 260]]
    target = 13
    res = Solution().searchMatrix(matrix, target)
    assert res == True

    matrix = [[13, 23, 25, 27], [210, 211, 216, 220], [223, 230, 234, 260]]
    target = 260
    res = Solution().searchMatrix(matrix, target)
    assert res == True

    matrix = [[13, 23, 25, 27], [210, 211, 216, 220], [223, 230, 234, 260]]
    target = 27
    res = Solution().searchMatrix(matrix, target)
    assert res == True

    matrix = [[13, 23, 25, 27], [210, 211, 216, 220], [223, 230, 234, 260]]
    target = 210
    res = Solution().searchMatrix(matrix, target)
    assert res == True

    matrix = [[], [], []]
    target = 13
    res = Solution().searchMatrix(matrix, target)
    assert res == False

    print(f"all done")
