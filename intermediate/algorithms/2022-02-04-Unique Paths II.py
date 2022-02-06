"""
From: https://leetcode.com/problems/unique-paths-ii/submissions/
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0

        n_rows = len(obstacleGrid)
        n_cols = len(obstacleGrid[0])
        num_paths = [[None]*n_cols
                     for i in range(n_rows)]
        for row in range(n_rows-1, -1, -1):
            for col in range(n_cols-1, -1, -1):
                if row == n_rows - 1 and col == n_cols - 1:
                    num_paths[row][col] = 1 - obstacleGrid[row][col]
                    continue
                if obstacleGrid[row][col] == 1:
                    num_paths[row][col] = 0
                    continue

                nps = 0
                if row < n_rows-1 and obstacleGrid[row+1][col] == 0:
                    nps += num_paths[row+1][col]
                if col < n_cols-1 and obstacleGrid[row][col+1] == 0:
                    nps += num_paths[row][col+1]
                num_paths[row][col] = nps

        # print(num_paths)
        return num_paths[0][0]


if __name__ == "__main__":
    assert Solution().uniquePathsWithObstacles([[0,0,0],[0,0,0],[0,0,0]])\
           == 6
    assert Solution().uniquePathsWithObstacles([[0,0,1],[0,0,0],[0,0,0]])\
           == 5
    assert Solution().uniquePathsWithObstacles([[0,0,0],[1,0,0],[0,0,0]])\
           == 3
    assert Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])\
           == 2
    assert Solution().uniquePathsWithObstacles([[0,0,0],[0,0,0],[0,0,1]])\
           == 0
    assert Solution().uniquePathsWithObstacles([[0,1],[0,0]])\
           == 1
    assert Solution().uniquePathsWithObstacles([[0,1],[1,0]])\
           == 0

    print(f"all done")
