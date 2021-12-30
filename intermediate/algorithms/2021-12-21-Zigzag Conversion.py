"""
From: https://leetcode.com/problems/zigzag-conversion/

"""
import pprint
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Encode zig zag
        i = 0
        sp = 0
        zigzag = []
        while sp < len(s):
            zigzag.append([""]*numRows)
            if i == 0:
                for j in range(numRows):
                    zigzag[-1][j] = s[sp]
                    sp += 1
                    if sp >= len(s):
                        break
                i = numRows - 2
            else:
                zigzag[-1][i] = s[sp]
                sp += 1
                i -= 1
        pprint.pprint(zigzag)

        # Extract from zig zag
        parts = []
        for row in range(numRows):
            for col in zigzag:
                parts.append(col[row])

        print(f"done")

        return "".join(parts)


if __name__ == "__main__":
    res = Solution().convert(s="PAYPALISHIRING", numRows=3)
    assert res == "PAHNAPLSIIGYIR"

    res = Solution().convert(s="PAYPALISHIRING", numRows=4)
    assert res == "PINALSIGYAHRPI"

    print(f"All done")