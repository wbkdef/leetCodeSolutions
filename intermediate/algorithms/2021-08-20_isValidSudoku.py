import itertools as it

# 2021-08-20
class Solution:
    def validate9(self, nine):
        assert len(nine) == 9
        joined = "".join(nine)
        return len(joined) == len(set(joined))

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        b = [[item.replace(".", "") for item in row] for row in board]

        to_validate = [row for row in b]
        for i in range(9):
            to_validate.append([row[i] for row in b])
        for x_start in [0, 3, 6]:
            for y_start in [0, 3, 6]:
                to_validate.append(list(
                    it.chain.from_iterable([row[x_start: x_start+3]
                                            for row in b[y_start: y_start+3]])))

        vals = [self.validate9(nine) for nine in to_validate]
        return all(vals)


if __name__ == '__main__':
    board = [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    assert Solution().isValidSudoku(board) == False

    board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    assert Solution().isValidSudoku(board) == True

    print(f"all passed")


# Nice online solution
class Solution_OTHERS:
    def isValidSudoku(self, board):
        for row in chain(board, zip(*board)):
            cand = [i for i in row if i != "."]
            if len(set(cand)) != len(cand): return False

        for x, y in product([1, 4, 7], [1, 4, 7]):
            cand = [board[x + i][y + j] for i, j in product([-1, 0, 1], [-1, 0, 1])]
            cand = [i for i in cand if i != "."]
            if len(set(cand)) != len(cand): return False

        return True