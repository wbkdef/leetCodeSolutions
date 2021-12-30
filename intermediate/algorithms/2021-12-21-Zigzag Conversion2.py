"""
From: https://leetcode.com/problems/zigzag-conversion/

Decided to go for a solution that scales independently of numRows
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Encode rows
        sp = 0
        rows = [{} for i in range(numRows)]
        for row_num, col in self.yield_indices(numRows):
            rows[row_num][col] = s[sp]
            sp += 1
            if sp >= len(s):
                break

        # Reading off
        parts = []
        for row in rows:
            for col in sorted(row):
                parts.append(row[col])
        return "".join(parts)

    def yield_indices(self, numRows)  ->  tuple[int, int]:
        col = -1
        while True:
            col += 1
            for row in range(numRows):
                yield row, col
            for col, row in enumerate(range(numRows - 2, 0, -1), col+1):
                yield row, col


if __name__ == "__main__":
    res = Solution().convert(s="PAYPALISHIRING", numRows=3)
    assert res == "PAHNAPLSIIGYIR"

    res = Solution().convert(s="PAYPALISHIRING", numRows=4)
    assert res == "PINALSIGYAHRPI"

    print(f"All done")